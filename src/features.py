"""Dataset validation and physics-informed feature construction."""
import numpy as np
import pandas as pd

RAW_NUMERIC = [
    "Air temperature [K]", "Process temperature [K]",
    "Rotational speed [rpm]", "Torque [Nm]", "Tool wear [min]",
]
ENGINEERED = [
    "Temperature Gradient", "Approximate Spindle Power",
    "Wear-Stress Index", "Speed-Torque Ratio",
    "TW Rolling Mean", "TW Rolling Std",
]
TYPE_DUMMIES = ["Type_L", "Type_M", "Type_H"]
REQUIRED = ["UDI", "Type", *RAW_NUMERIC, "Machine failure"]


def validate_dataset(df: pd.DataFrame) -> None:
    missing = sorted(set(REQUIRED) - set(df.columns))
    if missing:
        raise ValueError(f"Dataset is missing required columns: {missing}")
    if len(df) != 10_000:
        raise ValueError(f"Expected 10,000 rows; found {len(df):,}")


def engineer_features(df: pd.DataFrame) -> pd.DataFrame:
    """Create the six features defined in the published framework."""
    out = df.copy().sort_values("UDI").reset_index(drop=True)
    out["Temperature Gradient"] = out["Process temperature [K]"] - out["Air temperature [K]"]
    out["Approximate Spindle Power"] = out["Torque [Nm]"] * out["Rotational speed [rpm]"] / 9550.0
    out["Wear-Stress Index"] = out["Tool wear [min]"] * out["Torque [Nm]"]
    out["Speed-Torque Ratio"] = out["Rotational speed [rpm]"] / np.maximum(out["Torque [Nm]"], 1e-5)
    out["TW Rolling Mean"] = out["Tool wear [min]"].rolling(50, min_periods=1).mean()
    out["TW Rolling Std"] = out["Tool wear [min]"].rolling(50, min_periods=1).std().fillna(0.0)
    dummies = pd.get_dummies(out["Type"], prefix="Type", dtype=float)
    for col in TYPE_DUMMIES:
        out[col] = dummies[col] if col in dummies else 0.0
    return out


ORIGINAL_FEATURES = [*RAW_NUMERIC, *TYPE_DUMMIES]
FULL_FEATURES = [*RAW_NUMERIC, *ENGINEERED, *TYPE_DUMMIES]

