# with open('sample.txt', 'r') as reader:
#     # Read & print the entire file
#     print(reader.read())

# with open('sample.txt', 'r') as reader:
#     # Read & print the partial file
#     print(reader.read(5))

# with open('sample.txt', 'r') as reader:
#     # Read & print the partial file
#     print(reader.readline(), end='')
#     print(reader.readline(), end='')
#     print(reader.readline(), end='')
#     print(reader.readline(), end='')

# with open('sample.txt', 'r') as reader:
#     # Read & print the partial file
#     print(reader.readline(5))
#     print(reader.readline(5))
#     print(reader.readline(5))
#     print(reader.readline(5))

# with open('sample.txt', 'r') as reader:
#     # Read & print the partial file
#     print(reader.readlines())

# file = open('sample.txt', 'r')
# data = file.read()
# print(data)
# file.close()

import pandas as pd
import csv
# with open('sample.csv', 'r') as myFile:
#     lines = csv.reader(myFile, delimiter=';')
#     for line in lines:
#         print(line)

# field1 = []
# field2 = []
# field3 = []
# with open('sample.csv', 'r') as myFile:
#     lines = csv.DictReader(myFile, delimiter=';')
#     for line in lines:
#         # print(line)
#         field1.append(line['Province/State'])
#         field2.append(line['Country/Region'])
#         field3.append(line['Last Update'])

# print("Field1 -", field1)
# print("Field2 -", field2)
# print("Field3 -", field3)

# df = pd.read_csv("sample.csv", delimiter=";")
# print(df)

# df = pd.read_excel("sample1.xlsx")
# print(df.head())
#
xlsx = pd.ExcelFile("sample1.xlsx")
# print(xlsx)
# Now you can list all sheets in the file
print(xlsx.sheet_names)

# to read just one sheet to dataframe
# df = pd.read_excel(xlsx, sheet_name='Sheet2')
# print(df)

# Import xlsx file and store each sheet in to a df object
dfs = {sheet_name: xlsx.parse(sheet_name) for sheet_name in xlsx.sheet_names}
# print(dfs)
sheetNames = list(dfs.keys())
# print(list(dfs.keys()))
df = dfs[sheetNames[0]]
print(df.head())

# dask.dataframe() - a large parallel Dataframe composed of many smaller Pandas Dataframes
# datatable - Python package for manipulating big 2-dimensional tabular data structures
