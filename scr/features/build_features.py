import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from DataTransformation import PrincipalComponentAnalysis

# ------------------------------------------------------
# Load data
# ------------------------------------------------------

# Load climate data
df = pd.read_pickle("../../data/interim/climate_df_imputedNA.pkl")


# ------------------------------------------------------
# Processing data for model
# ------------------------------------------------------

# Select the column to model (Max_T)
select_df = df.copy().drop(
    columns=[
        "Station",
        "ID",
        "Year",
        "Month",
        "Day",
        "Min_T",
        "Mean_T",
        "HDD",
        "Precip_T",
    ]
)

# ------------------------------------------------------
# Save processed data
# ------------------------------------------------------

# Save climate data to processed folder in a pickle format
select_df.to_pickle("../../data/processed/climate_df_model.pkl")

# ------------------------------------------------------
# Principal Component Analysis Example
# ------------------------------------------------------

# Make a copy of the DF
df_pca = df.copy()

# Drop columns that are not needed for PCA
df_pca = df_pca.drop(columns=["Station", "ID"])
# Get all columns to perform PCA
pred_columns = list(df_pca.columns[3:])
# Create an instance of the PCA class
PCA = PrincipalComponentAnalysis()
# Perform PCA and return explained variance
pc_values = PCA.determine_pc_explained_variance(df_pca, pred_columns)

# Plot the explained variance
plt.figure(figsize=(10, 5))
plt.plot(range(1, len(pred_columns) + 1), pc_values, "bo-", linewidth=2)
plt.xlabel("Number of Components")
plt.ylabel("Variance (%)")
plt.show()

# Perform PCA on the selected columns and return the transformed DF
df_pca = PCA.apply_pca(df_pca, pred_columns, 2)
