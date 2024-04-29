import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

class MeteoriteMap:
    def __init__(self, data_frame):
        self.meteorite_data = data_frame

    def clean_data(self):
        """Cleans the meteorite data by removing rows where coordinates are zero or out of valid range."""
        cleaned_data = self.meteorite_data[(self.meteorite_data['reclat'] != 0.0) | (self.meteorite_data['reclong'] != 0.0)]
        cleaned_data = cleaned_data[(cleaned_data['reclat'] >= -90) & (cleaned_data['reclat'] <= 90) &
                                    (cleaned_data['reclong'] >= -180) & (cleaned_data['reclong'] < 180)]
        return cleaned_data

    def plot_data(self):
        """Plots the cleaned meteorite data based on classification."""
        cleaned_data = self.clean_data()
        classification_colors = {
            'OC': 'blue',
            'CC': 'green',
            'EC': 'red',
            'IR': 'purple',
            'AC': 'orange',
            'SI': 'darkred',
            'PA': 'lightblue',
            'KC': 'darkgreen',
            'Unclassified/ ungrouped meteorites': 'pink',
            'Unknown': 'gray',
            'Relict': 'cadetblue',
            'Lunar meteorite': 'black'
        }

        fig, ax = plt.subplots(figsize=(12, 8))
        scatter = ax.scatter(
            x=cleaned_data['reclong'],
            y=cleaned_data['reclat'],
            c=cleaned_data['classification_group'].map(classification_colors),
            s=50,  # Adjust the size of the points
            alpha=0.6  # Adjust transparency of the points
        )

        plt.title('Meteorite Landings by Classification')
        plt.xlabel('Longitude')
        plt.ylabel('Latitude')
        plt.grid(True)
        plt.show()

