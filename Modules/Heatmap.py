import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

class MeteoriteHeatMap:
    def __init__(self, data_frame):
        """Initialize with a pandas DataFrame."""
        self.meteorite_data = data_frame

    def plot_heat_map(self):
        """Plots a heat map of meteorite landing locations."""
        plt.figure(figsize=(12, 6))
        sns.kdeplot(
            x=self.meteorite_data['reclong'],
            y=self.meteorite_data['reclat'],
            cmap="Reds",
            fill=True
        )
        plt.title('Heat Map of Meteorite Landing Locations')
        plt.xlabel('Longitude')
        plt.ylabel('Latitude')
        plt.grid(True, which='both', linestyle='--', linewidth=0.5)
        plt.show()


