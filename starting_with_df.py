import pandas as pd

data = {
    'name': ['Xavier', 'Ann', 'Jana', 'Yi', 'Robin', 'Amal', 'Nori'],
    'city': ['Mexico City', 'Toronto', 'Prague', 'Shanghai',
             'Manchester', 'Cairo', 'Osaka'],
    'age': [41, 28, 33, 34, 38, 31, 37],
    'py-score': [88.0, 79.0, 81.0, 80.0, 68.0, 61.0, 84.0]
}

index = range(101, 108)

df = pd.DataFrame(data, index=index)

cities = df['city']

# print(df)               # prints the whole table data incl. index

# print(df.head())        # prints the first 5 rows

# print(df.tail())        # prints the last 5 rows

# print(df.head(3))       # prints the first 3 rows

# print(df['city'])       # prints all the cities from the data incl. index

# print(df.index)         # prints the range index

# print(df.loc[103])      # prints out the data with index 103

# print(cities[103])      # prints the city from index 103
