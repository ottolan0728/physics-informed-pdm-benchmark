# Reproducibility protocol

The executable implementation follows the fixed configurations in Table 6 of the published article. It intentionally does not preserve the experimental settings found in the earlier development notebook (IF 200 trees with contamination 0.034 and XGBoost 300 trees at learning rate 0.05), because those settings do not match the published specification.

## Leakage controls

The 80:20 stratified partition is created before scaling or oversampling. `StandardScaler` is fitted only on training observations, and SMOTE is applied only to the scaled training partition. The untouched test partition is used for all reported rerun metrics.

## Categorical variable

Machine type is one-hot encoded (`Type_L`, `Type_M`, and `Type_H`) as stated in Table 9. This replaces the ordinal 0/1/2 encoding in the legacy development notebook.

## Rolling features

Rows are ordered by `UDI`; a trailing window of 50 observations with no future values is used for tool-wear rolling mean and standard deviation. This is the convention preserved from the available implementation.

## Reference versus rerun results

Files in `results/published/` are transcriptions of values printed in the published article or its final figures. They provide an auditable reference, not a claim that the repository reran the experiment during packaging. Fresh executions write only to `results/generated/`.

Latency is hardware- and software-dependent. Exact latency agreement with Table 10 is therefore not expected; predictive metrics should be compared separately from timing.

