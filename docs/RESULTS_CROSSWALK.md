# Paper-to-repository crosswalk

| Published item | Reference artifact | Executable path |
|---|---|---|
| Table 6 fixed configurations | `src/config.py` | `src.run_experiment.make_model` |
| Physics-informed features | — | `src/features.py` |
| Table 9 MI scores | `results/published/table_09_mi_scores.csv` | reference values |
| Table 10 model comparison | `results/published/table_10_benchmark_results.csv` | `python -m src.run_experiment` |
| Figure 14 F1 ablation | `results/published/figure_14_f1_ablation.csv` | both feature-set runs |
| Figure 15 MCC comparison | final image in `figures/` | generated metrics include MCC |
| Figure 16 confusion matrices | final image in `figures/` | generated metrics and predictions |
| Figure 17 XGBoost importance | `results/published/figure_17_feature_importance.csv` and final image | reference values |

The final article contains additional Figure 17 variables not present in the public AI4I 2020 schema (for example vibration, acoustic-emission, force, coolant-pressure, and surface-quality variables). The supplied final figure and its values are preserved as a published reference. The AI4I-only executable does not fabricate these unavailable inputs.

