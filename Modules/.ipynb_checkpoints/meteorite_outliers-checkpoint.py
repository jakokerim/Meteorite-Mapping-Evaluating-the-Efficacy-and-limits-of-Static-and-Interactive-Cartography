import pandas as pd

class MeteoriteOutliers:
    def __init__(self, data_frame):
        self.meteorite_data = data_frame

    def find_out_of_bounds_lat(self):
        """Find meteorite data entries with latitude values out of bounds."""
        return self.meteorite_data[(self.meteorite_data['reclat'] < -90) | (self.meteorite_data['reclat'] > 90)]

    def find_out_of_bounds_long(self):
        """Find meteorite data entries with longitude values out of bounds."""
        return self.meteorite_data[(self.meteorite_data['reclong'] < -180) | (self.meteorite_data['reclong'] >= 180)]

    def find_total_outliers(self):
        """Find total meteorite data entries with latitude or longitude values out of bounds."""
        return self.meteorite_data[(self.meteorite_data['reclat'] < -90) | (self.meteorite_data['reclat'] > 90) |
                                   (self.meteorite_data['reclong'] < -180) | (self.meteorite_data['reclong'] >= 180)]

    def report_outliers(self):
        """Print a report of meteorite data entries with out of bounds latitude and longitude values."""
        out_of_bounds_lat = self.find_out_of_bounds_lat()
        out_of_bounds_long = self.find_out_of_bounds_long()
        outliers = self.find_total_outliers()

        print(f"Number of outliers in latitude: {out_of_bounds_lat.shape[0]}")
        print(f"Number of outliers in longitude: {out_of_bounds_long.shape[0]}")
        print(f"Total number of outliers: {outliers.shape[0]}")
        print(outliers)
