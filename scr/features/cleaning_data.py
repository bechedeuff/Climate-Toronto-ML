import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# ------------------------------------------------------
# Load data
# ------------------------------------------------------

# Load climate data
df = pd.read_pickle("../../data/interim/climate_df.pkl")

df.info()

# ------------------------------------------------------
# Fill missing values with interpolation
# ------------------------------------------------------

# Get all columns to fill missing values
predictor_columns = list[df.columns[5:]]

# Fill missing values with interpolation
for col in predictor_columns:
    df[col] = df[col].interpolate()

# Check DF info
df.info()

# Save climate data to interim folder in a pickle format
df.to_pickle("../../data/interim/climate_df_imputedNA.pkl")

# ------------------------------------------------------
# Fill missing values with mean
# ------------------------------------------------------

# Fill Mat_T, Min_T, Mean_T, HDD, Precip_T with mean
df["Max_T"] = df["Max_T"].fillna(df["Max_T"].mean())
df["Min_T"] = df["Min_T"].fillna(df["Min_T"].mean())
df["Mean_T"] = df["Mean_T"].fillna(df["Mean_T"].mean())
df["HDD"] = df["HDD"].fillna(df["HDD"].mean())
df["Precip_T"] = df["Precip_T"].fillna(df["Precip_T"].mean())

# Save climate data to interim folder in a pickle format
df.to_pickle("../../data/interim/weather_df_noNA.pkl")
