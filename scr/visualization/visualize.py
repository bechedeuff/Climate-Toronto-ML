import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style("white")

# ------------------------------------------------------
# Load data
# ------------------------------------------------------

# Load weather data
df = pd.read_pickle("../../data/interim/climate_df.pkl")

# ------------------------------------------------------
# Plot single column
# ------------------------------------------------------

# Plot min temperature
df.plot(y="Min_T", figsize=(15, 5))

# Plot missing values
df.isna().sum().plot(kind="bar", figsize=(15, 5))

# ------------------------------------------------------
# Plot multiple columns in one plot with multiple figures
# ------------------------------------------------------

# Plot min and max temperatures with sns
fig, ax = plt.subplots(figsize=(15, 5))
ax.plot(df["Min_T"], label="Min Temp")
ax.plot(df["Max_T"], label="Max Temp")
ax.set_title("Min and Max Temperature")

for l in df["Year"].unique():
    subset = df[df["Year"] == l]
    fig, ax = plt.subplots(figsize=(15, 5))
    ax.plot(subset["Min_T"], label="Min Temp")
    ax.plot(subset["Max_T"], label="Max Temp")
    ax.set_title(f"Min and Max Temperature for {l}")
    plt.legend()
    plt.show()


# Combine plots in one figure
fig, ax = plt.subplots(nrows=5, sharex=True, figsize=(25, 10))
ax[0].plot(df["Min_T"], label="Min Temp")
ax[0].legend()
ax[1].plot(df["Max_T"], label="Max Temp", color="red")
ax[1].legend()
ax[2].plot(df["Mean_T"], label="Mean Temp", color="purple")
ax[2].legend()
ax[3].plot(df["HDD"], label="Heating Degree Day", color="orange")
ax[3].legend()
ax[4].plot(df["Precip_T"], label="Precipitation", color="cyan")
ax[4].legend()
ax[0].set_title("Weather Data")


# ------------------------------------------------------
# Groupby year
# ------------------------------------------------------

# Plot min temperature grouped by year
climate_year = df.groupby(["Year"])["Min_T"].plot(figsize=(15, 5), legend=True)
