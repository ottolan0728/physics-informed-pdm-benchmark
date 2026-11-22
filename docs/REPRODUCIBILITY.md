# Reproducibility protocol and independent-rerun scope

## What the repository can and cannot establish

This repository contains the public executable implementation of the *Sensors* 2026 paper, with fixed benchmark configurations corresponding to Table 6. The values in `results/published/` are **transcribed article references**, not fresh output from the script. An independent clean rerun has succeeded, but its metrics do **not** exactly reproduce published Table 10. The original historical per-row predictions, environment and experiment provenance remain unavailable.

## Data and split

Obtain the third-party AI4I 2020 dataset from its original distribution and place `ai4i2020.csv` at `data/ai4i2020.csv`. A recovered 10,000-row, 14-column local CSV had SHA-256 `dc6630cd9b1f0f853922fad78a1b6436570d3f1ec863f1dd5c4340ac56bc8a8e`; this hash has not been independently matched against the upstream distributor.

The script uses stratified 80:20 sampling with random seed 42. StandardScaler is fitted to training observations only. Oversampling, where used, is applied only to the training subset. The untouched test labels are used for final evaluation, not for selecting thresholds.

## Model-specific training procedure

| Model | Imbalance handling |
|---|---|
| Logistic Regression | Balanced class weights; no SMOTE |
| Isolation Forest | Unsupervised; no SMOTE |
| Random Forest | Training-only SMOTE plus balanced class weights |
| XGBoost | Training-only SMOTE |

These are model-specific procedures; they are **not** one identical resampling method for every learner. The published Table 6 configuration uses IF 100 estimators and contamination auto. The older development notebook had IF 200 estimators/contamination 0.034 and a different XGBoost setup. Those legacy settings should not be substituted silently.

## Feature representation and interpretation

The executable code one-hot encodes Machine Type into Type_L, Type_M and Type_H. The paper's Eq. (7) describes ordinal 0/1/2 encoding, while its Table 8 refers to one-hot encoding and counts raw feature categories. Accordingly, the expanded numerical design matrix does not have the same column count as the conceptual 12-feature table.

Six derived features include temperature gradient, approximate spindle power, wear–stress index, speed–torque ratio, and rolling mean/standard deviation of tool wear. Rolling features are constructed from UDI-ordered records before the random split, using trailing windows. This creates sample-context dependence across the eventual partitions, even though scaler fitting and SMOTE remain train-only. The AI4I records should not be treated as validated chronological equipment trajectories.

## Independent rerun versus publication

A clean rerun in Python 3.13 yielded physics-informed F1: LR 0.3183, IF 0.1531, RF 0.6871 and XGBoost 0.6994. The article's Table 10 reports LR 0.324, IF 0.266, RF 0.722 and XGBoost 0.580. These differences are unresolved and must not be erased by test-set threshold tuning or by replacing published reference values.

The original prescribed Python 3.11 environment has **not** been independently verified. Inference latency is also hardware- and software-dependent.

## Running the code

```bash
pip install -r requirements.txt
python -m src.run_experiment
```

Run from the repository root after obtaining the dataset. Generated metrics and predictions are written to `results/generated/` and remain gitignored. The legacy notebook is a thin launcher without saved outputs. A separately prepared executed companion is under author review.

For the article-to-code mapping, see [RESULTS_CROSSWALK.md](RESULTS_CROSSWALK.md).
