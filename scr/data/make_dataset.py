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
    df = pd.concat((pd.read_csv(f, index_col="Date/Time", parse_dates=True) for f in all_files))
    df = df.dropna(axis=1, how="all")
    df = df.drop(df.columns[df.columns.str.contains("Flag")], axis=1)
    df = df.drop(
        ["Snow on Grnd (cm)", "Longitude (x)", "Latitude (y)", "Cool Deg Days (°C)"],
        axis=1,
    )
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
climate_df = import_climate_data()

# Save weather data to interim folder in a pickle format
climate_df.to_pickle(save_path + "climate_df.pkl")
