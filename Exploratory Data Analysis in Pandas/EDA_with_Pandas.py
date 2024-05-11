import pandas as pd
import seaborn as sns 
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv(r"C:\Users\User\Desktop\tinashe beans. Data Nerd\Exploratory Data Analysis in Pandas\dataset\world_population.csv")

pd.set_option('display.float_format', lambda x: '%.2f' %x)

#getting infomation about the data set
df.info()
print(df.describe())
print(df.isnull().sum())
print(df.nunique())

#sorting the datframe by population to find the top 5 countries with the highest population
df.sort_values(by=['2022 Population'], ascending=False, inplace= True)

# finding the correlation between the Population values
numeric_columns = df.select_dtypes(include=[np.number])
correlation_matrix = numeric_columns.corr
print(correlation_matrix())
#print(df.head().to_string())