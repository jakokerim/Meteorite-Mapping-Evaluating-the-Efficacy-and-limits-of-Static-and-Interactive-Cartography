import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

class MeteoriteVisualization:
    def __init__(self, data_frame):
        """Initialize with a pandas DataFrame."""
        self.meteorite_data = data_frame

    def clean_data(self):
        """Clean the meteorite data by removing zero coordinates and filtering invalid lat-long."""
        cleaned_data = self.meteorite_data[(self.meteorite_data['reclat'] != 0.0) | (self.meteorite_data['reclong'] != 0.0)]
        cleaned_data = cleaned_data[(cleaned_data['reclat'] >= -90) & (cleaned_data['reclat'] <= 90) &
                                    (cleaned_data['reclong'] >= -180) & (cleaned_data['reclong'] < 180)]
        return cleaned_data

    def plot_meteorite_landings(self):
        """Plot meteorite landings by classification on a scatter plot."""
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

        ax = cleaned_data.plot(
            x="reclong", 
            y="reclat", 
            kind="scatter", 
            c=cleaned_data['classification_group'].map(classification_colors),
            colorbar=False, 
            title='Meteorite Landings by Classification'
        )
        legend_labels = [mpatches.Patch(color=color, label=classification) for classification, color in classification_colors.items()]
        plt.legend(handles=legend_labels, loc='upper left', bbox_to_anchor=(1,1), title="Classifications")

        plt.show()
