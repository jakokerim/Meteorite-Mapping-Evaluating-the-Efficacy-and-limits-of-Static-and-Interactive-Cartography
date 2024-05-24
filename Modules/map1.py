import pandas as pd
import folium
from folium.plugins import MarkerCluster

def filter_meteorite_data(meteorite_data):
    """Filter out meteorite data rows with missing or zero latitude/longitude."""
    df_filtered = meteorite_data.dropna(subset=['reclat', 'reclong'])
    df_filtered = df_filtered[~((df_filtered['reclat'] == 0) & (df_filtered['reclong'] == 0))]
    df_filtered['year'] = df_filtered['year'].fillna(0).astype(int)
    df_filtered = df_filtered[(df_filtered['reclat'] >= -90) & (df_filtered['reclat'] <= 90) &
                              (df_filtered['reclong'] >= -180) & (df_filtered['reclong'] <= 180)]
    
    return df_filtered

def generate_meteorite_map(df_filtered):
    """Generate a Folium map with meteorite landings."""
    m = folium.Map(location=[0, 0], zoom_start=2)
    marker_cluster = MarkerCluster(maxClusterRadius=40).add_to(m)

    for idx, row in df_filtered.iterrows():
        popup_text = (f"{row['name']}<br>"
                      f"Type: {row['classification_group']}<br>"
                      f"Mass: {row['mass (g)']}g<br>"
                      f"Year: {row['year']}")
        folium.Marker(
            location=[row['reclat'], row['reclong']],
            popup=popup_text,
        ).add_to(marker_cluster)

    return m
# Explanation : Loop Through DataFrame: The function iterates over each row in the DataFrame df_filtered using iterrows().
# Popup Text:
#    For each row, it constructs a string popup_text that includes the meteorite's name, classification group, mass, and year.
# Add Marker:
#    A folium.Marker is created for each meteorite, using its latitude (reclat) and longitude (reclong) for the location.
#    The marker includes a popup with the constructed popup_text.## 