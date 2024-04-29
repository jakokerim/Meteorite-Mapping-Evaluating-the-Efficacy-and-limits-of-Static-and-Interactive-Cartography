# meteorite_cleaner.py

import pandas as pd

class Cleaner:
    def __init__(self, data_frame):
        self.meteorite_data = data_frame

    def clean_data(self):
        """Remove entries with zero coordinates and those outside valid latitude and longitude ranges."""
        # Remove entries where both latitude and longitude are zero
        cleaned_data = self.meteorite_data[(self.meteorite_data['reclat'] != 0.0) & (self.meteorite_data['reclong'] != 0.0)]
        cleaned_data = self.meteorite_data.dropna(subset=['reclat', 'reclong'])
        # Further clean data to ensure all entries are within valid latitude and longitude ranges
        cleaned_data = cleaned_data[(cleaned_data['reclat'] >= -90) & (cleaned_data['reclat'] <= 90) &
                                    (cleaned_data['reclong'] >= -180) & (cleaned_data['reclong'] < 180)]
        return cleaned_data



