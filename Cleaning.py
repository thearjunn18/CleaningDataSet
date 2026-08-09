#importing the modules
import numpy as np
import pandas as pd

#loading the dataset
object_= pd.read_csv("/Users/arjunsharma/DatabaseCleaning/dirty_employee_dataset_30.csv")
print(object_.head())

#checking the missing values 
print("Missing Values in each coloume")
print(object_.isnull().sum())
