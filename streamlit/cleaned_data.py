
import pandas as pd

class Cleaner:
    def __init__(self, data_frame):
        self.meteorite_data = data_frame

    def clean_data(self):
        cleaned_data = self.meteorite_data.copy()
        cleaned_data['year'] = cleaned_data['year'].fillna(0).astype(int)
        cleaned_data = cleaned_data.dropna(subset=['reclat', 'reclong'])
        cleaned_data = cleaned_data[~((cleaned_data['reclat'] == 0) & (cleaned_data['reclong'] == 0))]
        cleaned_data = cleaned_data.dropna(subset=['reclat', 'reclong'])
        cleaned_data = cleaned_data[(cleaned_data['reclat'] >= -90) & (cleaned_data['reclat'] <= 90) &
                                    (cleaned_data['reclong'] >= -180) & (cleaned_data['reclong'] < 180)]
        return cleaned_data
