from turtle import color
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ------------------------------------------------------
# Load data
# ------------------------------------------------------

# Load weather data
weather_df = pd.read_pickle("../../data/interim/weather_df.pkl")

# ------------------------------------------------------
# Plot single column
# ------------------------------------------------------

# Plot min temperature
weather_df.plot(y="Min_T", figsize=(15, 5))

# ------------------------------------------------------
# Plot multiple columns in one plot with multiple figures
# ------------------------------------------------------

# Plot min and max temperatures with sns
sns.set_style("white")
fig, ax = plt.subplots(figsize=(15, 5))
ax.plot(weather_df["Min_T"], label="Min Temp")
ax.plot(weather_df["Max_T"], label="Max Temp")
ax.set_title("Min and Max Temperature")

for l in weather_df["Year"].unique():
    subset = weather_df[weather_df["Year"] == l]
    fig, ax = plt.subplots(figsize=(15, 5))
    ax.plot(subset["Min_T"], label="Min Temp")
    ax.plot(subset["Max_T"], label="Max Temp")
    ax.set_title(f"Min and Max Temperature for {l}")
    plt.legend()
    plt.show()


# Combine plots in one figure
sns.set_style("white")
fig, ax = plt.subplots(nrows=5, sharex=True, figsize=(25, 10))
ax[0].plot(weather_df["Min_T"], label="Min Temp")
ax[0].legend()
ax[1].plot(weather_df["Max_T"], label="Max Temp", color="red")
ax[1].legend()
ax[2].plot(weather_df["Mean_T"], label="Mean Temp", color="purple")
ax[2].legend()
ax[3].plot(weather_df["HDD"], label="Heating Degree Day", color="orange")
ax[3].legend()
ax[4].plot(weather_df["Precip_T"], label="Precipitation", color="cyan")
ax[4].legend()
ax[0].set_title("Weather Data")


# ------------------------------------------------------
# Groupby year
# ------------------------------------------------------

# Plot min temperature grouped by year
weather_year = weather_df.groupby(["Year"])["Min_T"].plot(figsize=(15, 5), legend=True)
