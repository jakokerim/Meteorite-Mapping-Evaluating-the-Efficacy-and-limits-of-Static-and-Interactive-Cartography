import pandas as pd

class DataQuality:
    def __init__(self, data):
        self.data = data

    def print_missing_values(self):                                                 
        """Print the count of missing values for each column in the DataFrame.""" 
        missing_values = self.data.isnull().sum()
        print("Missing Values:")
        print(missing_values)
        print()

    def print_zero_values(self):
        """Print the count of zero values for each column in the DataFrame."""
        zero_values = (self.data == 0).sum()
        print("Zero Values in Each Column:")
        print(zero_values)

    def count_zero_lat_long(self):
        """Count and print the number of rows where both 'reclat' and 'reclong' are zero."""
        zero_lat_long_count = ((self.data['reclat'] == 0.0) & (self.data['reclong'] == 0.0)).sum()
        print("Count of rows with 'reclat' and 'reclong' both equal to 0:", zero_lat_long_count)

    def print_duplicate_rows(self):
        """Print the count of duplicate rows in the DataFrame."""
        duplicate_rows = self.data.duplicated().sum()
        print("Duplicate Rows:")
        print(duplicate_rows)
        print()

    def print_unique_values(self):
        """Print the count of unique values for each column in the DataFrame."""
        unique_values = {column: self.data[column].nunique() for column in self.data.columns}
        print("Unique Values:")
        print(unique_values)