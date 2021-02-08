#Description: predict the direction of a Cripto Price#Description: predict the direction of a Cripto Price

#Import Lighbary
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

#Load the data set
#from google.colab import files
#files.upload()

#Store the Data into the data frame
df = pd.read_csv("bitcoin-historical-data - Sheet1.csv")

#Show data frame
df

print(df)

