import folium
import streamlit as st
from folium.plugins import Search
from streamlit_folium import st_folium
from folium.plugins import Draw

def create_map_with_input(cleaned_data):


    # Initialize the map
    m = folium.Map(location=[0, 0], zoom_start=2)

    Draw(export=True).add_to(m)

    
    # Add markers
    feature_group = folium.FeatureGroup(name="Meteorites").add_to(m)
    for idx, row in cleaned_data.iterrows():
        popup_text = f"{row['name']}<br>Mass: {row['mass (g)']}g<br>Year: {row['year']}"
        feature = folium.GeoJson(
            data={
                "type": "Feature",
                "properties": {
                    "name": row['name'],
                    "popup": popup_text
                },
                "geometry": {
                    "type": "Point",
                    "coordinates": [row['reclong'], row['reclat']]
                }
            },
            tooltip=row['name']
        ).add_child(folium.Popup(popup_text))
        
        feature_group.add_child(feature)

    # Add search feature to the map
    search = Search(
        layer=feature_group,
        search_label='name',  # Ensure 'name' is the property used for search
        placeholder='Search for Meteorite Name',
        collapsed=True,
    ).add_to(m)

    return m     

