# Importing modules
import numpy as np
import pandas as pd


# Loading the dataset
object_ = pd.read_csv("dirty_employee_dataset_30.csv")

print("Original Dataset:")
print(object_.head())


# -------------------------------
# 1. CHECK MISSING VALUES
# -------------------------------

print("\nMissing Values Before Cleaning:")
print(object_.isnull().sum())


# -------------------------------
# 2. REPLACE INFINITE VALUES
# -------------------------------

object_.replace([np.inf, -np.inf], np.nan, inplace=True)


# -------------------------------
# 3. HANDLE INVALID VALUES
# -------------------------------

# Year of experience cannot be negative
object_.loc[
    object_["year_of_experience"] < 0,
    "year_of_experience"
] = np.nan


# Age cannot be negative or unrealistic
object_.loc[
    (object_["age"] < 18) | (object_["age"] > 65),
    "age"
] = np.nan


# Salary cannot be negative or zero
object_.loc[
    object_["salary"] <= 0,
    "salary"
] = np.nan


# Performance ratio should be between 0 and 2
object_.loc[
    (object_["performance_ratio"] < 0) |
    (object_["performance_ratio"] > 2),
    "performance_ratio"
] = np.nan


# -------------------------------
# 4. FILL MISSING VALUES
# -------------------------------

object_["year_of_experience"] = object_["year_of_experience"].fillna(
    object_["year_of_experience"].median()
)

object_["age"] = object_["age"].fillna(
    object_["age"].median()
)

object_["salary"] = object_["salary"].fillna(
    object_["salary"].median()
)

object_["performance_ratio"] = object_["performance_ratio"].fillna(
    object_["performance_ratio"].median()
)


# -------------------------------
# 5. CHECK CLEANED DATA
# -------------------------------

print("\nMissing Values After Cleaning:")
print(object_.isnull().sum())


# -------------------------------
# 6. SAVE CLEAN DATASET
# -------------------------------

object_.to_csv("Cleaned_DataSet.csv", index=False)

print("\nData cleaning is completed!")
print("Cleaned file saved as Cleaned_DataSet.csv")