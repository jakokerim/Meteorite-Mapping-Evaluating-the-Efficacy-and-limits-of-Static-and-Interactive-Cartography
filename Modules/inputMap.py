import folium
from folium.plugins import Search
import pandas as pd

def create_map_with_input(meteorite_data):
    n_samples = int(input("Enter the number of random samples you want to display: "))  # User enters the number of points
    
    # Data filtering
    df_filtered = meteorite_data.dropna(subset=['reclat', 'reclong'])
    df_filtered = df_filtered[(df_filtered['reclat'] != 0) | (df_filtered['reclong'] != 0)]
    df_filtered['year'] = df_filtered['year'].fillna(0).astype(int)
    df_filtered = df_filtered[(df_filtered['reclat'] >= -90) & (df_filtered['reclat'] <= 90) &
                              (df_filtered['reclong'] >= -180) & (df_filtered['reclong'] <= 180)]
    # Select random samples
    df_sampled = df_filtered.sample(n=min(n_samples, len(df_filtered)), random_state=None)

    # Initialize the map
    m = folium.Map(location=[0, 0], zoom_start=2)

    # Classification colors
    classification_colors = {
        'OC': 'blue', 'CC': 'green', 'EC': 'red', 'IR': 'purple',
        'AC': 'orange', 'SI': 'darkred', 'PA': 'lightblue',
        'KC': 'darkgreen', 'Unclassified/ ungrouped meteorites': 'pink',
        'Unknown': 'gray', 'Relict': 'cadetblue', 'Lunar meteorite': 'black'
    }

    # Add markers
    feature_group = folium.FeatureGroup(name="Meteorites").add_to(m)
    for idx, row in df_sampled.iterrows():
        popup_text = f"{row['name']}<br>Type: {row['classification_group']}<br>Mass: {row['mass (g)']}g<br>Year: {row['year']}"
        marker_color = classification_colors.get(row['classification_group'], 'gray')
        feature = folium.GeoJson(
            data={
                "type": "Feature",
                "properties": {
                    "name": row['name'],
                    "popup": popup_text,
                    "style": {"color": marker_color, "fillColor": marker_color}
                },
                "geometry": {
                    "type": "Point",
                    "coordinates": [row['reclong'], row['reclat']]
                }
            },
            tooltip=row['name'],
            style_function=lambda x: {"color": x["properties"]["style"]["color"]}
        ).add_child(folium.Popup(popup_text))
        
        feature_group.add_child(feature)

# Add search feature
    search = Search(
        layer=feature_group,
        search_label='name',
        placeholder='Search for Meteorite Name',
        collapsed=True,
        position='topright'
    ).add_to(m)

    return m
        
        