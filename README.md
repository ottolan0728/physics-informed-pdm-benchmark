# Physics-Informed Benchmarking Framework for Predictive Maintenance

Official implementation repository associated with:

> Yi-Kai Su and Chun-Jan Tseng, “A Physics-Informed Benchmarking Framework for Machine Learning and Tree-Based Ensembles in IIoT-Enabled Predictive Maintenance,” *Sensors*, 26(16), 5026, 2026. https://doi.org/10.3390/s26165026

This repository implements the public AI4I 2020 benchmark using Logistic Regression, Isolation Forest, Random Forest and XGBoost with six engineering-derived features.

**Reproducibility status (November 2026):** The published Table 10 values in `results/published/` are transcriptions from the article. An independently executed rerun of this repository on the recovered 10,000-row AI4I dataset produced different F1 values: LR 0.3183, IF 0.1531, RF 0.6871 and XGBoost 0.6994, versus published 0.324, 0.266, 0.722 and 0.580. The original historical prediction records have not been recovered; exact numerical replication is **not established**. See [results crosswalk](docs/RESULTS_CROSSWALK.md) and [reproducibility protocol](docs/REPRODUCIBILITY.md).

## Quick start

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
```

Download the third-party [AI4I 2020 Predictive Maintenance dataset](https://www.kaggle.com/datasets/stephanmatzka/predictive-maintenance-dataset-ai4i-2020) and place `ai4i2020.csv` at `data/ai4i2020.csv`. The dataset is not redistributed here.

```bash
python -m src.run_experiment
```

The lightweight [notebook launcher](notebooks/reproduce_paper.ipynb) invokes the same script. A fully executed independent companion notebook has been prepared separately for author review; it is not part of this repository until verified and uploaded.

Fresh outputs are written to `results/generated/` (gitignored). Published reference values in `results/published/` are never overwritten.

## Protocol scope

- Stratified 80:20 train–test split, random seed 42.
- Scaling fitted on the training partition only; testing labels are not used for fitting or threshold selection.
- **Model-specific imbalance handling:** Logistic Regression uses balanced class weights; Isolation Forest is unsupervised; Random Forest uses train-only SMOTE plus balanced class weights; XGBoost uses train-only SMOTE.
- The implementation uses one-hot machine-type encoding and six derived features; this expands the numerical design matrix beyond the raw-variable count used in the paper's Table 8.
- Tool-wear rolling statistics use ordered observations and are constructed before the split. Their sample-context dependency is documented, and they should not be interpreted as independent chronological sequences.
- Accuracy, precision, recall, F1, ROC-AUC, balanced accuracy, MCC, confusion matrices and latency are generated for the independent rerun.

See [REPRODUCIBILITY.md](docs/REPRODUCIBILITY.md) and [RESULTS_CROSSWALK.md](docs/RESULTS_CROSSWALK.md).

## Repository layout

```text
src/                 public executable implementation
notebooks/           lightweight notebook launcher
data/                instructions for obtaining third-party AI4I data
results/published/   article values (reference only)
results/generated/   independent local rerun outputs (gitignored)
figures/             published figures
docs/                protocol, provenance and results mapping
tests/               implementation checks
```

## Citation

Su, Y.-K., & Tseng, C.-J. (2026). A Physics-Informed Benchmarking Framework for Machine Learning and Tree-Based Ensembles in IIoT-Enabled Predictive Maintenance. *Sensors, 26*(16), 5026. https://doi.org/10.3390/s26165026

See [CITING.md](CITING.md) and [CITATION.cff](CITATION.cff) for additional formats.

## License

Code and documentation are released under the MIT License. Reuse of article figures is governed by the published article's license.
