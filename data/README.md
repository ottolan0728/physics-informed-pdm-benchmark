# Dataset

This repository does not redistribute the AI4I 2020 dataset.

1. Download the CSV from the [Kaggle dataset page](https://www.kaggle.com/datasets/stephanmatzka/predictive-maintenance-dataset) (accessed 26 June 2026 for the published study).
2. Save it as `data/ai4i2020.csv`.
3. Verify that it contains 10,000 rows and the columns `UDI`, `Type`, `Air temperature [K]`, `Process temperature [K]`, `Rotational speed [rpm]`, `Torque [Nm]`, `Tool wear [min]`, and `Machine failure`.

The executable validates these fields before training.

