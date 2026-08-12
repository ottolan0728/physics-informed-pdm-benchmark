"""Frozen Table 6 benchmark configuration."""
SEED = 42
TEST_SIZE = 0.20
ROLLING_WINDOW = 50

MODEL_CONFIG = {
    "LR": {"penalty": "l2", "solver": "lbfgs", "max_iter": 1000},
    "IF": {"n_estimators": 100, "contamination": "auto", "random_state": SEED},
    "RF": {"n_estimators": 200, "max_depth": None, "random_state": SEED},
    "XGBoost": {
        "n_estimators": 200, "learning_rate": 0.10,
        "max_depth": 6, "subsample": 0.8, "random_state": SEED,
    },
}

