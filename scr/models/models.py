from calendar import c
from pyexpat.errors import XML_ERROR_NOT_STANDALONE
from turtle import color
from venv import create
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import xgboost as xgb
from sklearn.metrics import mean_squared_error

plt.style.use("fivethirtyeight")
color_pal = sns.color_palette()

# ------------------------------------------------------
# Load data
# ------------------------------------------------------

# Load weather data
df = pd.read_pickle("../../data/processed/climate_df_model.pkl")

# ------------------------------------------------------
# Plot data
# ------------------------------------------------------

df.plot(figsize=(15, 5), color=color_pal[0], title="Max Temperature Toronto City")

# ------------------------------------------------------
# Train / Test split
# ------------------------------------------------------

train = df.loc[df.index < "01-01-2020"]
test = df.loc[df.index >= "01-01-2020"]

fig, ax = plt.subplots(figsize=(15, 5))
train.plot(ax=ax, label="Training Set", title="Data Train/Test Split")
test.plot(ax=ax, label="Test Set")
ax.axvline("01-01-2020", color="black", linestyle="--", lw=1)
ax.legend(["Training Set", "Test Set"])
plt.show()

# ------------------------------------------------------
# Checking week data
# ------------------------------------------------------

df.loc[(df.index >= "01-01-2020") & (df.index < "01-08-2020")].plot()

# ------------------------------------------------------
# Create features
# ------------------------------------------------------


def create_feature(df):
    """
    Create time series features based on time series index
    """
    df = df.copy()
    df["Quarter"] = df.index.quarter
    df["Month"] = df.index.month
    df["DayofYear"] = df.index.dayofyear
    df["DayofMonth"] = df.index.day
    df["Year"] = df.index.year
    return df


df_maxT_model = create_feature(df)

# ------------------------------------------------------
# Visualize our Feature / Target Relationship
# ------------------------------------------------------

fig, ax = plt.subplots(figsize=(15, 5))
sns.boxplot(data=df_maxT_model, x="Quarter", y="Max_T", ax=ax)
ax.set_title("Max Temperature by Quarter")

fig, ax = plt.subplots(figsize=(15, 5))
sns.boxplot(data=df_maxT_model, x="Month", y="Max_T", ax=ax)
ax.set_title("Max Temperature by Month")

# ------------------------------------------------------
# Create model
# ------------------------------------------------------
train = create_feature(train)
test = create_feature(test)

features = ["Quarter", "Month", "DayofYear", "DayofMonth", "Year"]
target = "Max_T"

X_train = train[features]
y_train = train[target]

X_test = test[features]
y_test = test[target]

reg = xgb.XGBRegressor(n_estimators=1000, early_stopping_rounds=50, learning_rate=0.05)
reg.fit(X_train, y_train, eval_set=[(X_train, y_train), (X_test, y_test)], verbose=10)

# ------------------------------------------------------
# Feature importance
# ------------------------------------------------------

fi = pd.DataFrame(
    data=reg.feature_importances_, index=reg.feature_names_in_, columns=["Importance"]
)
fi.sort_values(by="Importance", ascending=True).plot(
    kind="barh", figsize=(15, 5), title="Feature Importance"
)
plt.show()

# ------------------------------------------------------
# Forecast on test
# ------------------------------------------------------

test["Prediction"] = reg.predict(X_test)

df_model = df_maxT_model.copy()
df_model = df_maxT_model.merge(
    test[["Prediction"]], how="left", left_index=True, right_index=True
)

ax = df_model["Max_T"].plot(figsize=(15, 5))
df_model["Prediction"].plot(ax=ax, color="red")
plt.legend(["Truth Data", "Prediction"])
ax.set_title("Raw Data and Prediction")
plt.show()


ax = df_model.loc[(df_model.index >= "01-01-2020") & (df_model.index < "01-08-2020")][
    "Max_T"
].plot(figsize=(15, 5), title="Week of Data")
df_model.loc[(df_model.index >= "01-01-2020") & (df_model.index < "01-08-2020")][
    "Prediction"
].plot(ax=ax, color="red")
plt.legend(["Truth Data", "Prediction"])
plt.show()

# ------------------------------------------------------
# Metrics and Evaluation
# ------------------------------------------------------

# Calculate RMSE
score = np.sqrt(mean_squared_error(test["Max_T"], test["Prediction"]))

# Calculate Error
test["Error"] = np.abs(test["Max_T"] - test["Prediction"])

# Worst and best predicted days
test.sort_values(by="Error", ascending=True).head(10)  # bests
test.sort_values(by="Error", ascending=False).head(10)  # worsts

# ------------------------------------------------------
# Next steps
# ------------------------------------------------------

# - Add more data
# - Add more features
# - Hyperparameter tuning
# - More robust cross validation
