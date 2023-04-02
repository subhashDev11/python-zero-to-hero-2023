import pandas as pd

# read a CSV file into a dataframe
df = pd.read_csv('file.csv')
print(df)

#inspecting data

# display the first 5 rows of the dataframe
print(df.head())

# display the last 5 rows of the dataframe
print(df.tail())

# display basic statistics of the dataframe
print(df.describe())


#Manipulating data:

# read a CSV file into a dataframe
df = pd.read_csv('file.csv')
df1 = pd.read_csv('file.csv')
df2 = pd.read_csv('file.csv')

# select a column from the dataframe
column = df['column_name']

# filter rows of the dataframe based on a condition
filtered_df = df[df['column_name'] > 10]

# group the dataframe by a column and aggregate another column
grouped_df = df.groupby('column_name')['another_column'].mean()

# merge two dataframes based on a common column
merged_df = pd.merge(df1, df2, on='column_name')

#Writing data:

# read a CSV file into a dataframe
df = pd.read_csv('file.csv')

# write the dataframe to a CSV file
df.to_csv('output.csv', index=False)
