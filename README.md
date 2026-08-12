# Physics-Informed Benchmarking Framework for Predictive Maintenance

Official reproducibility repository for:

> Yi-Kai Su and Chun-Jan Tseng, “A Physics-Informed Benchmarking Framework for Machine Learning and Tree-Based Ensembles in IIoT-Enabled Predictive Maintenance,” *Sensors*, 26(16), 5026, 2026. https://doi.org/10.3390/s26165026

The framework evaluates Logistic Regression, Isolation Forest, Random Forest, and XGBoost on the AI4I 2020 Predictive Maintenance dataset. It augments the original sensor variables with six engineering-derived features and evaluates the effect of those features under severe class imbalance.

## Quick start

```bash
python -m venv .venv
# Windows: .venv\\Scripts\\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
```

Download `ai4i2020.csv` from the [AI4I 2020 Predictive Maintenance dataset](https://www.kaggle.com/datasets/stephanmatzka/predictive-maintenance-dataset) and place it at `data/ai4i2020.csv`. The dataset is not redistributed by this repository.

Run the complete workflow:

```bash
python -m src.run_experiment
```

Generated artifacts are written to `results/generated/`. Published reference values transcribed from the paper are stored separately in `results/published/` and are never overwritten.

## Reproducibility scope

- Fixed random seed: 42
- Stratified 80:20 train–test split
- Standardization fitted on the training partition only
- SMOTE applied to the training partition only
- Model configurations follow Table 6 of the published article
- Both original-only and original-plus-physics-informed feature sets are evaluated
- Accuracy, precision, recall, F1, ROC-AUC, balanced accuracy, MCC, confusion matrices, and per-sample latency are exported

See [REPRODUCIBILITY.md](docs/REPRODUCIBILITY.md) for the protocol and [RESULTS_CROSSWALK.md](docs/RESULTS_CROSSWALK.md) for the paper-to-repository mapping.

## Repository layout

```text
src/                 executable implementation
notebooks/           thin notebook entry point
data/                dataset acquisition instructions
results/published/   values reported in the article
results/generated/   local rerun outputs (gitignored)
figures/              final published figures
docs/                 protocol, provenance, and crosswalk
tests/                feature-engineering and configuration checks
```

## How to cite

If this repository, its code, or its published benchmark results support your work, please cite the associated article:

> Su, Y.-K., & Tseng, C.-J. (2026). A Physics-Informed Benchmarking Framework for Machine Learning and Tree-Based Ensembles in IIoT-Enabled Predictive Maintenance. *Sensors, 26*(16), 5026. https://doi.org/10.3390/s26165026

Available citation paths:

- Full APA, IEEE, and BibTeX formats: [CITING.md](CITING.md)
- Machine-readable GitHub citation metadata: [CITATION.cff](CITATION.cff)
- Publisher page and permanent DOI: [https://doi.org/10.3390/s26165026](https://doi.org/10.3390/s26165026)
- On GitHub, select **Cite this repository** in the repository sidebar to export the citation metadata.

## License

Code and documentation are released under the MIT License. Figure reuse remains subject to the published article's license.
