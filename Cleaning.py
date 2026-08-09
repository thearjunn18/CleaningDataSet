#importing the modules
import numpy as np
import pandas as pd

#loading the dataset
object_= pd.read_csv("/Users/arjunsharma/DatabaseCleaning/dirty_employee_dataset_30.csv")
print(object_.head())

#checking the missing values 
print("Missing Values in each coloume")
print(object_.isnull().sum())

#filling the missssing values
object_["year_of_experience"].fillna(object_["year_of_experience"].mean(), inplace = True)
object_["salary"].fillna(object_["salary"].mean(), inplace = True)
object_["performance_ratio"].fillna(object_["performance_ratio"].mean(), inplace = True)
object_["year_of_experience"].fillna(object_["year_of_experience"].median(), inplace = True)

#filling infinite values , negative values 
object_.replace([np.inf, -np.inf] , np.nan, inplace=True)
object_.fillna(object_.mean(), inplace=True)
object_["year_of_experience"].fillna(object_["year_of_experience"].mean(), inplace = True)
object_["salary"].fillna(object_["salary"].mean(), inplace = True)
object_["performance_ratio"].fillna(object_["performance_ratio"].mean(), inplace = True)
object_["year_of_experience"].fillna(object_["year_of_experience"].median(), inplace = True)

#creating new file 
object_.to_csv("Cleaned_DataSet.csv", index=False)
print("Data cleaning is completed ")