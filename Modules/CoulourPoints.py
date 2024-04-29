import pandas as pd
import folium
from folium.plugins import MarkerCluster

def process_data(meteorite_data):
    """Process meteorite data to filter and prepare for mapping."""
    df_filtered = meteorite_data.dropna(subset=['reclat', 'reclong'])
    df_filtered = df_filtered[~((df_filtered['reclat'] == 0) & (df_filtered['reclong'] == 0))]
    df_filtered['year'] = df_filtered['year'].fillna(0).astype(int)
    df_filtered = df_filtered[(df_filtered['reclat'] >= -90) & (df_filtered['reclat'] <= 90) &
                              (df_filtered['reclong'] >= -180) & (df_filtered['reclong'] <= 180)]
    return df_filtered

def create_map(df_filtered):
    """Create and return a Folium map with meteorite locations marked."""
    m = folium.Map(location=[0, 0], zoom_start=2)
    marker_cluster = MarkerCluster().add_to(m)
    
    classification_colors = {
        'OC': 'blue', 'CC': 'green', 'EC': 'red', 'IR': 'purple',
        'AC': 'orange', 'SI': 'darkred', 'PA': 'lightblue', 'KC': 'darkgreen',
        'Unclassified/ ungrouped meteorites': 'pink', 'Unknown': 'gray',
        'Relict': 'cadetblue', 'Lunar meteorite': 'black'
    }
    
    for idx, row in df_filtered.iterrows():
        popup_text = f"{row['name']}<br>Type: {row['classification_group']}<br>Mass: {row['mass (g)']}g<br>Year: {row['year']}"
        marker_color = classification_colors.get(row['classification_group'], 'gray')
        folium.Marker(
            location=[row['reclat'], row['reclong']],
            popup=popup_text,
            icon=folium.Icon(color=marker_color)
        ).add_to(marker_cluster)
    return m
