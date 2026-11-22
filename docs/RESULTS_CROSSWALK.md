# Published results versus executable outputs

**Important:** A published-reference file is not proof of an independently reproduced result. `results/published/` transcribes article tables and figures; `results/generated/` contains local rerun artifacts.

| Published item | Published reference | Executable or limitation |
|---|---|---|
| Table 6 configurations | `src/config.py` | `src.run_experiment.make_model`; see model-specific protocols |
| Engineering-derived features | Article §3.3 | `src/features.py`; one-hot categorical expansion |
| Table 9 MI scores | `results/published/table_09_mi_scores.csv` | Published reference; not a verified identical rerun |
| Table 10 model comparison | `results/published/table_10_benchmark_results.csv` | `python -m src.run_experiment` generates different independent values |
| Figure 14 F1 ablation | `results/published/figure_14_f1_ablation.csv` | Original and physics-informed feature-set reruns |
| Figure 15 MCC comparison | Published figure in `figures/` | Independent generated metrics include MCC |
| Figure 16 confusion matrices | Published figure in `figures/` | Independent generated predictions and matrices; not historical originals |
| Figure 17 feature importance | `results/published/figure_17_feature_importance.csv` | Published reference only for non-AI4I sensor channels |

## Table 10 F1 crosswalk

| Model | Published | Independent clean rerun (Python 3.13) |
|---|---:|---:|
| Logistic Regression | 0.324 | 0.3183 |
| Isolation Forest | 0.266 | 0.1531 |
| Random Forest | 0.722 | 0.6871 |
| XGBoost | 0.580 | 0.6994 |

The rerun is a real execution of the released code but **not** an exact historical replication of the article's values. The original predictions and full historical execution environment have not been recovered. An independent Python 3.11 pinned-environment rerun remains outstanding.

## Figure 17 boundary

The final published Figure 17 includes variables absent from the public AI4I 2020 schema, including vibration, acoustic emission, force, coolant pressure and surface quality. Those published figure values are preserved as historical references; the AI4I-only executable does not synthesize unavailable measurements.

## Model and feature definition caveats

The published Eq. (7) describes ordinal machine type; Table 8 refers to one-hot, and the code uses one-hot. The expanded design matrix has more columns than the paper's raw-variable count. Rolling statistics are calculated on UDI-ordered observations before splitting, so derived features can depend on observations later assigned to another partition. Model-specific imbalance handling is documented in [REPRODUCIBILITY.md](REPRODUCIBILITY.md).
