import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

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
