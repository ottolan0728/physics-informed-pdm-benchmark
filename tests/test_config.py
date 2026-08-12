from src.config import MODEL_CONFIG


def test_table6_configuration():
    assert MODEL_CONFIG["IF"]["n_estimators"] == 100
    assert MODEL_CONFIG["IF"]["contamination"] == "auto"
    assert MODEL_CONFIG["RF"]["n_estimators"] == 200
    assert MODEL_CONFIG["XGBoost"]["n_estimators"] == 200
    assert MODEL_CONFIG["XGBoost"]["learning_rate"] == 0.10
    assert MODEL_CONFIG["XGBoost"]["subsample"] == 0.8

