import pandas as pd
from glob import glob

# Paths
file_path = "../../data/raw/*.csv"
save_path = "../../data/interim/"


# Function to import weather data
def import_climate_data():
    """
    Function to import all weather data from the raw folder
    and drop unnecessary columns.
    """
    all_files = glob(file_path)
    df = pd.concat(
        (pd.read_csv(f, index_col="Date/Time", parse_dates=True) for f in all_files)
    )
    df = df.dropna(axis=1, how="all")
    df = df.drop(df.columns[df.columns.str.contains("Flag")], axis=1)
    df = df.drop("Snow on Grnd (cm)", axis=1)
    df = df.drop(["Longitude (x)", "Latitude (y)"], axis=1)
    df = df.drop(["Cool Deg Days (°C)"], axis=1)
    df = df.rename(
        columns={
            "Station Name": "Station",
            "Climate ID": "ID",
            "Max Temp (°C)": "Max_T",
            "Min Temp (°C)": "Min_T",
            "Mean Temp (°C)": "Mean_T",
            "Heat Deg Days (°C)": "HDD",
            "Total Precip (mm)": "Precip_T",
        }
    )

    return df


# Calling function to import weather data
weather_df = import_climate_data()

# Save weather data to interim folder in a pickle format
weather_df.to_pickle(save_path + "climate_df.pkl")


# ------------------------------------------------------
# STEP-BY-STEP
# ------------------------------------------------------


# ------------------------------------------------------
# Read single CSV file

single_file_weather = pd.read_csv(
    "../../data/raw/en_climate_daily_ON_6158355_2015_P1D.csv"
)

single_file_weather = single_file_weather.set_index("Date/Time")

pd.to_datetime(single_file_weather.index, format="%Y-%m-%d")

single_file_weather.info()

single_file_weather.index

single_file_weather.plot(y="Min Temp (°C)", figsize=(15, 5))

# ------------------------------------------------------
# Read multiple CSV files

# Get all CSV files in the folder
all_files = glob("../../data/raw/*.csv")

# Import all CSV in a DF
df = pd.concat(
    (pd.read_csv(f, index_col="Date/Time", parse_dates=True) for f in all_files)
)

# Drop NA columns
df = df.dropna(axis=1, how="all")

# Drop columns that has flag in the name
df = df.drop(df.columns[df.columns.str.contains("Flag")], axis=1)

# Drop Snow on grnd (cm) column
df = df.drop("Snow on Grnd (cm)", axis=1)

# Drop Lon and lat columns
df = df.drop(["Longitude (x)", "Latitude (y)"], axis=1)

# DF info
df.info()


# ------------------------------------------------------
# Check for missing values

# Total precipitation (mm) NAs
df["Total Precip (mm)"].isna().sum()

# Fill NAs with mean
df["Total Precip (mm)"] = df["Total Precip (mm)"].fillna(df["Total Precip (mm)"].mean())
