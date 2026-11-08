import pandas as pd


def analyze_users(users):
    dataframe = pd.DataFrame.from_records(users)
    print("Shape (rows, columns):", dataframe.shape)
    print("\nFirst two records:")
    print(dataframe.head(2))
    print("\nLast two records:")
    print(dataframe.tail(2))

    return dataframe