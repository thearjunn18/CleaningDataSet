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
object_["year_of_experience"].fillna(object_["year_of_experience"].mean(), implace = True)
object_["salary"].fillna(object_["salary"].mean(), implace = True)
object_["performance_ratio"].fillna(object_["performance_ratio"].mean(), implace = True)
object_["year_of_experience"].fillna(object_["year_of_experience"].median(), implace = True)
