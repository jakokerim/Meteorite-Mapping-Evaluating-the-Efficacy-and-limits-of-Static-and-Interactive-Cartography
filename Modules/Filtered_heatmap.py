import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class MeteoriteHeatMap:
    def __init__(self, data_frame):
        """Initialize with a pandas DataFrame."""
        self.meteorite_data = data_frame

    def clean_data(self):
        """Clean the meteorite data by removing rows where coordinates are zero or out of valid range."""
        cleaned_data = self.meteorite_data[(self.meteorite_data['reclat'] != 0.0) | (self.meteorite_data['reclong'] != 0.0)]
        cleaned_data = cleaned_data[(cleaned_data['reclat'] >= -90) & (cleaned_data['reclat'] <= 90) &
                                    (cleaned_data['reclong'] >= -180) & (cleaned_data['reclong'] < 180)]
        return cleaned_data

    def plot_heat_map(self):
        """Plots a heat map of cleaned meteorite landing locations."""
        cleaned_data = self.clean_data()
        plt.figure(figsize=(12, 6))
        sns.kdeplot(
            x=cleaned_data['reclong'],
            y=cleaned_data['reclat'],
            cmap="Reds",
            fill=True
        )
        plt.title('Heat Map of Meteorite Landing Locations')
        plt.xlabel('Longitude')
        plt.ylabel('Latitude')
        plt.grid(True, which='both', linestyle='--', linewidth=0.5)
        plt.show()

