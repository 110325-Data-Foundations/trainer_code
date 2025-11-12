# Pandas 
# A python library for working with large data sets, to do data analysis. 
# We will be working with just one data set, and for now we'll just write a .py file.

# However it is common to use pandas and other data analysis tools inside something 
# like a Jupyter notebook. 

# First step to working with data in Pandas: we have to read it in. 

# Imports 
import pandas as pd # Import-as: lets us alias the module/class with an easier to reference name

# Read our csv
df = pd.read_csv("./data/Electric_Vehicle_Population_Data.csv")

# Pandas has built in methods for reading our data in - we don't need to go
# through the File IO that we saw last week. 

# That .read_csv() method produces a data frame, we need to store it in a variable
# in order to work with it. 

# A data-frame is just a pythonic object representation of our data. Its organized
# as rows and columns, with each column having a title. Our rows are our individual
# entries in our data set. 

# They are mutable - so we can alter them after they are created. They are technically 
# built on NumPy arrays. Columns can be of different data types, and we can decide the data
# types and change them as needed. 

# We can create dataframes from datasets like JSONs or CSVs, as well as assemble them in code
# from python lists or dictionaries or NumPy arrays. 

# Inspecting data 
print(df.head().to_string()) # attempting to read the first five entries in our dataframe. 

# df.info() # df.info() - gives us metadata about our data set. Columns, non-null counts, data types, etc

print(df.describe()) # Gives us some summary info about the data in our data set. Things like count, mean
# standard deviation, etc. 
print(df.shape) # Gives us the total number of rows, as well as the total number of columns. 


# Beyond inspecting, we can work with our data - we can select individual rows and columns, filter, etc. 

#df.loc() and df.iloc() - Loc is label based selection, iloc is index based selection. 

print(df.loc[1]) # Selecting a single row 

print(df.iloc[1: 100]) # Selecting a slice of entries from the data set

print(df['Make']) # Selecting everything in one column, accessing it via name. 

# df['Make'] - I can select all the info in a column either by referencing the column name 
# or its index in the dataframe. However once i do that, what comes back is no longer a dataframe.
# Dataframes are 2D, what comes back is a Series - essentially a list. 

print(df.loc[ 0:5, ['City', "Postal Code"]]) # Example of df.loc - We need how many things to select, as well as a collection
# of column names. With df.loc and df.iloc - we can create dataframes that contain selected subsets of our larger
# data set. 

# Data Cleaning
# Sometimes our data sets contain null values - we want to explicitly handle them. Or atleast be aware of them.
# We can view how many rows of our dataset (in our dataframe) have nulls, and we can even sub in some default value
# for those nulls before we try to do anything else with our data. This is referred to as data cleaning. 

print(df.isna().sum()) # We ca use df.isna to select cells that contain null values

# Beyond subbing in some default value, we can also just select drop rows that contain nulls. 

# To replace missing values with some specific value use .fillna()
df.fillna(0)  

# We can get more granular and go column by column if we need to - just depends on the data set and your use case. 
df.dropna() # Dropping rows that contain any missing values - can be valid, you will lose data in the data frame. 




print(tesla_df.info())