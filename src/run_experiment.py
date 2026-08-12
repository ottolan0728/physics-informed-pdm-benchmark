"""Run Table 6 models and the original-vs-physics-informed ablation."""
from pathlib import Path
from time import perf_counter
import json
import numpy as np
import pandas as pd
from imblearn.over_sampling import SMOTE
from sklearn.ensemble import IsolationForest, RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (accuracy_score, balanced_accuracy_score, confusion_matrix,
    f1_score, matthews_corrcoef, precision_score, recall_score, roc_auc_score)
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from xgboost import XGBClassifier
from .config import MODEL_CONFIG, SEED, TEST_SIZE
from .features import FULL_FEATURES, ORIGINAL_FEATURES, engineer_features, validate_dataset

ROOT = Path(__file__).resolve().parents[1]


def make_model(name):
    cfg = dict(MODEL_CONFIG[name])
    if name == "LR": return LogisticRegression(class_weight="balanced", random_state=SEED, **cfg)
    if name == "IF": return IsolationForest(**cfg)
    if name == "RF": return RandomForestClassifier(class_weight="balanced", n_jobs=-1, **cfg)
    return XGBClassifier(eval_metric="logloss", n_jobs=-1, **cfg)


def main():
    source = ROOT / "data" / "ai4i2020.csv"
    out = ROOT / "results" / "generated"
    out.mkdir(parents=True, exist_ok=True)
    df = pd.read_csv(source); validate_dataset(df); df = engineer_features(df)
    y = df["Machine failure"].astype(int).to_numpy()
    indices = np.arange(len(df))
    train_idx, test_idx = train_test_split(indices, test_size=TEST_SIZE, random_state=SEED, stratify=y)
    rows, pred_frames = [], []
    for set_name, columns in {"Original": ORIGINAL_FEATURES, "Physics-informed": FULL_FEATURES}.items():
        scaler = StandardScaler()
        x_train = scaler.fit_transform(df.loc[train_idx, columns])
        x_test = scaler.transform(df.loc[test_idx, columns])
        y_train, y_test = y[train_idx], y[test_idx]
        x_smote, y_smote = SMOTE(random_state=SEED).fit_resample(x_train, y_train)
        for name in MODEL_CONFIG:
            model = make_model(name)
            fit_x, fit_y = (x_train, None) if name == "IF" else ((x_smote, y_smote) if name in {"RF", "XGBoost"} else (x_train, y_train))
            if name == "IF": model.fit(fit_x)
            else: model.fit(fit_x, fit_y)
            start = perf_counter()
            if name == "IF":
                pred = (model.predict(x_test) == -1).astype(int); score = -model.score_samples(x_test)
            else:
                pred = model.predict(x_test); score = model.predict_proba(x_test)[:, 1]
            latency = (perf_counter() - start) * 1000 / len(x_test)
            tn, fp, fn, tp = confusion_matrix(y_test, pred).ravel()
            rows.append({"feature_set": set_name, "model": name,
                "accuracy": accuracy_score(y_test,pred), "precision": precision_score(y_test,pred,zero_division=0),
                "recall": recall_score(y_test,pred,zero_division=0), "f1": f1_score(y_test,pred,zero_division=0),
                "roc_auc": roc_auc_score(y_test,score), "balanced_accuracy": balanced_accuracy_score(y_test,pred),
                "mcc": matthews_corrcoef(y_test,pred), "latency_ms_per_sample": latency,
                "tn":int(tn), "fp":int(fp), "fn":int(fn), "tp":int(tp)})
            pred_frames.append(pd.DataFrame({"row_index":test_idx,"UDI":df.loc[test_idx,"UDI"],
                "feature_set":set_name,"model":name,"y_true":y_test,"y_pred":pred,"y_score":score}))
    pd.DataFrame(rows).to_csv(out / "benchmark_and_ablation_metrics.csv", index=False)
    pd.concat(pred_frames, ignore_index=True).to_csv(out / "test_predictions.csv", index=False)
    (out / "run_metadata.json").write_text(json.dumps({"seed":SEED,"test_size":TEST_SIZE,"model_config":MODEL_CONFIG},indent=2),encoding="utf-8")
    print(pd.DataFrame(rows).round(4).to_string(index=False))


if __name__ == "__main__": main()

