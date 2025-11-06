# a collection of functions that is comman used
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
#==========Functions section========
# fist function to plot a barlpto for a given dataframe and dedects missing values
def plot_missing_values(data_f ):
    missing_v= data_f.isna().sum() # return a Series of columns and thier missing values count
    missing_v= missing_v[ missing_v> 0] # filter out the columns that have missing values
 #If there are missing values, plot them
    if not missing_v.empty:
        plt.figure(figsize=(10, 5))
        sns.barplot(x=missing_v.index, y=missing_v.values)
        plt.xticks(rotation=45, ha='right')
        plt.title('Missing Values per Column')
        plt.xlabel('Columns')
        plt.ylabel('Number of Missing Values')
        plt.show()
    else:
        print("No missing values found in the dataset.")
