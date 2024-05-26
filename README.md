# Meteorite Mapping: Evaluating the Efficacy and Limits of Static and Interactive Cartography

## Project Overview

This project aims to enhance the study of meteorites by leveraging advanced data visualization techniques. Using NASA’s extensive meteorite landings dataset, we have created a comprehensive platform that integrates both static and interactive visualizations through Jupyter Notebooks and Streamlit. The final product is a web-based application that offers detailed insights into meteorite landings, their distribution, and their impact on Earth.

## Table of Contents

- Introduction
- Dataset
- Installation
- Usage
- Features
- Modules
- Results
- Maintenance 
- Acknowledgements

## Introduction

Meteorites, remnants of meteoroids that have collided with Earth, provide profound insights into the early solar system. Understanding their distribution, frequency, and impact locations can significantly enhance our knowledge of cosmic phenomena and Earth's geological history. This project utilizes NASA’s meteorite landings dataset to create static and interactive visualizations, pushing the boundaries of what can be achieved within the Jupyter and Streamlit environments.
## Dataset

The dataset used in this study is provided by NASA and is publicly available on Data.gov. It includes approximately 45,000 unique observations of meteorite landings across the globe. The data columns include:

- **Name**: Each meteorite's name, usually based on the location where it was found.
- **ID**: A unique identifier for each meteorite.
- **Nametype**: Status of the meteorite (valid or not).
- **Recclass**: Classification of meteorites according to their composition.
- **Mass (g)**: Weight of the meteorite in grams.
- **Fall**: Indicates whether the meteorite was observed falling or was found later.
- **Year**: The year the meteorite fell or was found.
- **Reclat**: Recorded latitude.
- **Reclong**: Recorded longitude.
- **GeoLocation**: Combination of latitude and longitude.

## Usage

In the terminal, navigate to the streamlit folder. Then use 'streamlit run Meteorites.py'. Ensure that streamlit, folium, and streamlit folium are installed. This should open a local host in your web browser.

Once the Streamlit application is running, it will open a local host in your web browser. The dashboard includes various features:

- **Basic Introduction**: Overview of the project and its goals.
- **Data Cleaning Screenshots**: Visual documentation of the data cleaning process.
- **Static Maps**: Initial visualizations of the dataset.
- **Interactive Maps**: Dynamic maps where users can upload their own datasets and interact with the data.

## Images

Ensure that the images required for the project are stored in the streamlit folder. The image paths used in the code are relative to this folder.
Features

- Heat Map: Displays the density of meteorite landings.
- Clustered Map: Shows meteorite landing sites with interactive clusters.
- Color-Coded Points: Visualizes meteorites based on their classification.
- Drawing Capabilities: Allows users to mark important locations and calculate distances.
- Search Functionality: Users can search for specific meteorites by name or other attributes.

## Modules

The project includes various modules to handle different aspects of the visualization and data processing:

- Data Quality: Handles missing values, zero values, and duplicate rows.
- Map Generation: Functions to create different types of maps.
- Meteorite Classification: Categorizes meteorites into broader family groups.

## Results

The interactive maps are generated once a file is uploaded to the application. Users can explore the results through interactive pages and select which map they want to interact with.

## Maintenance

Regular maintenance is crucial to keep the application functional and up-to-date:

- Update Dependencies: Periodically review and update the codebase to ensure compatibility with new versions of Folium and Streamlit.


## Acknowledgements

This project utilized resources and data provided by NASA and leveraged open-source tools like Jupyter, Streamlit, and Folium. Special thanks to the contributors and the research community for their support and feedback.


