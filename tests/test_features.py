import pandas as pd
from src.features import engineer_features


def test_engineered_values():
    df = pd.DataFrame({"UDI":[1],"Type":["L"],"Air temperature [K]":[300.0],
        "Process temperature [K]":[310.0],"Rotational speed [rpm]":[955.0],
        "Torque [Nm]":[10.0],"Tool wear [min]":[5.0],"Machine failure":[0]})
    out = engineer_features(df).iloc[0]
    assert out["Temperature Gradient"] == 10.0
    assert out["Approximate Spindle Power"] == 1.0
    assert out["Wear-Stress Index"] == 50.0
    assert out["Type_L"] == 1.0

