import os
import pandas as pd
import streamlit as st
import folium
from streamlit_folium import st_folium
from folium.plugins import HeatMap

from cleaned_data import Cleaner
from map1 import generate_meteorite_map
from meteorite_classification import classify_meteorites
from CoulourPoints import create_map_colour
from inputMap import create_map_with_input

st.set_page_config(page_title='Meteorite Mapping: Evaluating the Efficacy and Limits of Static and Interactive Cartography', layout="wide")

def load_data(file_path):
    data = pd.read_csv(file_path, dtype={'year': str})
    return data

# Initialize session state variables if not already initialized
if 'last_selection_mode' not in st.session_state:
    st.session_state.last_selection_mode = None
if 'last_uploaded_file' not in st.session_state:
    st.session_state.last_uploaded_file = None
if 'last_sample_size' not in st.session_state:
    st.session_state.last_sample_size = 100  # Default value
if 'data_sample' not in st.session_state:
    st.session_state.data_sample = None
if 'full_data' not in st.session_state:
    st.session_state.full_data = None
if 'last_meteorite_names' not in st.session_state:
    st.session_state.last_meteorite_names = ''

# Define the base path for images
base_path = os.path.join(os.path.dirname(__file__), 'Screen shot AP')

image_path = os.path.join(base_path, 'Dalle.png')
missing_values_image_path = os.path.join(base_path, 'Missingvalues.png')
uniqueval = os.path.join(base_path, 'uniquevalue.png')
classification_image_path = os.path.join(base_path, 'meteor.jpg')
count = os.path.join(base_path, 'count.png')
Staticmap = os.path.join(base_path, 'Static map.png')
StaticHeatMap = os.path.join(base_path, 'Static Heat Map.png')
mix = os.path.join(base_path, 'Mix.png')
Landing_by_classification_HTML = os.path.join(base_path, 'Landing by classification HTML.png')

def main():
    st.title('Meteorite Mapping: Evaluating the Efficacy and Limits of Static and Interactive Cartography')
    st.image(image_path, caption="Image generated using OpenAI's DALL-E 3 model", use_column_width=True)

    # Adjusting the text size and style using HTML and CSS
    st.markdown("""
    <style>
    .intro {
        font-size: 14px;
        line-height: 1.6;
    }
    .motivation, .data-description {
        font-size: 14px;
        line-height: 1.6;
    }
    .notebook-list {
        font-size: 14px;
        line-height: 1.6;
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="intro">
    Welcome to this Streamlit Page and the project in general. Here you mostly can find interactive mapping, this page also contains static mapping that are available Jupyter Notebooks on: <a href="https://github.com/jakokerim/NASA.git">Github</a>. These Notebooks are designed to run and display code before integrating it into Streamlit. The Notebooks and the Streamlit code use a folder containing various modules called "Modules". Modules have their own needed libraries in their respective file as well as some explanation about codes. Multiple Notebooks are included in this project to build diverse codes and incorporate numerous features into the final model. Additionally, the extensive memory and processing power required to initialize Folium and plot points, necessitated dividing the project into different Notebooks. The Notebooks should be read in the following order:
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <ol class="notebook-list">
        <li><b>Intro_analysis</b>: This Notebook provides a comprehensive explanation of data inspection and cleaning, along with static visualizations.</li>
        <li><b>1HeatMap+map1</b>: The first use of Folium is showcased here, featuring a Heatmap and a display of the entire clustered dataset.</li>
        <li><b>2ColourPoints</b>: This Notebook re-displays the entire dataset in clusters, with each point color-coded according to the meteorite type.</li>
        <li><b>4NotWorking</b>: The first part of this Notebook displays a map with colored points and clusters, and includes an initial attempt to integrate a search bar. However, due to some issues, the code does not function correctly. We attempt to resolve this by displaying all the data. <b>NOTE</b>: This last code should not be run on average computers as it is too resource-intensive and may cause Nuvolos to crash. It illustrates what could have been achieved if the full dataset was displayed.</li>
        <li><b>5Input</b>: To interact with the data, this Notebook creates a map that prompts the user for the number of inputs to display. To make the search bar functional, we make some trade-offs between previously computed features.</li>
        <li><b>6Random</b>: Similar to the previous Notebook, but the number of inputs is selected directly in the code.</li>
        <li><b>7Draw</b>: This final Notebook combines the codes from the previous Notebooks. It includes search features, the ability to hover over points to display meteorite names without clicking, and a drawing capability.</li>
    </ol>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="motivation">
    <b>Motivation</b><br><br>
    Meteorites, the surviving fragments from meteoroids that have collided with Earth, provide invaluable insights into the early solar system. Studying their distribution, frequency, and impact locations can enhance our understanding of cosmic phenomena and Earth's geological history. Therefore this project studies how mapping could be used and implemented in coding environments, and evaluates the efficacy and limits of static and interactive mapping.
    </div>
    """, unsafe_allow_html=True)


    st.markdown("""
    <div class="data-description">
    <b>Data description</b><br><br>
    This project utilizes a dataset provided by NASA and hosted on <a href="https://data.gov/">Data.gov</a>, which encompasses records of meteorite landings across the globe.<br><br>
    The data is formatted in various files format, but in this project we will use the csv file due to its simple compatibility with Jupyter. The dataset is composed of some 45,000 unique observations. Indeed a meteorite can only land once on the Earth. The columns are composed of:<br><br>
    <ul>
        <li>Name: each meteorite has its own name, usually the name of the place where it fell</li>
        <li>ID: each meteorite has a unique identifier</li>
        <li>Nametype: no official meaning, but all the dataset is marked by valid</li>
        <li>Recclass: meteorites are classified according to their composition</li>
        <li>Mass (g): the weight of the meteorite in grams</li>
        <li>Fall: two possibilities:
            <ul>
                <li>Fell: observed meteorites as they fall to Earth</li>
                <li>Found: not observed but discovered later</li>
            </ul>
        </li>
        <li>Year: when the meteorite either fell to Earth or was found, depending on the context</li>
        <li>Reclat: recorded latitude</li>
        <li>Reclong: recorded longitude</li>
        <li>GeoLocation: Mix of latitude and longitude</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("""
    <div class="missing-values">
    <b>Missing values</b><br><br>
    In order to work properly with the data, it is important to filter information, especially the missing and zero values of each column, look for duplicates, and check how many unique values we have for each column. We have to be careful with the GeoLocation column, because it is composed of a tuple which includes (reclat, reclong). Therefore, the following code will show that there are no zero values in the GeoLocation column. However, this is false. To find out how many GeoLocation lines have the values (0.0, 0.0), we can count how many lines have 0.0 for reclat and 0.0 for reclong.
    </div>
    """, unsafe_allow_html=True)

    st.image(missing_values_image_path, caption="Missing values analysis", use_column_width=True)

    st.markdown("""
    This code displays clearly a few problems in the dataset:

    There are missing values in a few columns. For the year, it is intuitive that the meteorite could not be dated by scientists. However, the missing values for mass and location are more challenging to explain due to their nature. The data provided by NASA is not clearly explained, so we can only make assumptions. For the mass, one possibility is that the landing site was discovered, but the meteorite was no longer present, making it impossible to weigh. Another assumption is that the meteorite exploded upon landing, leaving no remnants to be found.

    To better understand the extent of these missing values, we can verify how many rows have missing values for Mass and GeoLocation.
    """)

    st.markdown("""
    Count of rows with missing values in both 'mass (g)' and 'GeoLocation': 12

    The output shows that only 12 meteorites have missing values for the mass and the location. It is not clear why in the data some values are missing.

    2. There are many columns with the value 0. As stated before NASA does not give a clear explanation on the data page for these values, but an assumption could be that the mass of the meteorite found is so close to 0 that it is easier to weight it to 0. However the values 0 in the GeoLocation column are confusing. It means that 6214 values fell into the exact same location. According to some documentation these meteorites have been discovered in Antartica and errors snuck into the dataset which classified the data at (0.0, 0.0). For this reason we will work without these values.

    The following Python code defines the MeteoriteData class using the Pandas library to manage meteorite data efficiently. It initializes with a file_path, allowing flexible data input, and provides methods like load_data to load the dataset into a DataFrame, and count_unique_recclass_values to count unique meteorite classifications after checking if data is loaded. This approach prevents errors from operations on unloaded data and enhances reusability. We use this code to explore the dataset and see how many unique values there is and how they called.
    """)
    st.image(uniqueval, caption="Unique values", use_column_width=False)

    st.markdown("""
<div class="meteorite-classification">
    <b>Meteorite Classification</b><br><br>
    We see in the previous code that there are 466 unique values, which means that, as of today, scientists have classified meteorites according to 466 different compositions.<br><br>
    Meteorites are classified into main groups based on their compositions and structures. Studies tend to disagree on classification methods, but here is a concise overview of the classifications:<br><br>
    <ul>
        <li><b>Stony Meteorites:</b>
            <ul>
                <li>Chondrites: These contain small spherical inclusions known as chondrules.
                    <ul>
                        <li>Carbonaceous Chondrites (CC): Includes subgroups like CI1 (Ivuna), CM2 (Mighei), and others.</li>
                        <li>Enstatite Chondrites (EC): Ranges from EH3 to EH5 (EH group) and EL3 to EL6 (EL group).</li>
                        <li>Ordinary Chondrites (OC): Includes H, L, LL groups, and unclassified types.</li>
                        <li>Kakangari Chondrites (KC): Notably the K3 (Kakangari group).</li>
                    </ul>
                </li>
                <li>Achondrites (AC): Lack chondrules and include types like Angrites (ANG), Eucrites (EUC), and others.</li>
                <li>Primitive Achondrites (PA): Such as Acapulcoites (ACA) and Winonaites (WIN).</li>
            </ul>
        </li>
        <li><b>Iron Meteorites:</b>
            <ul>
                <li>Classified by their nickel-iron alloy composition, with groups ranging from IA to IC and ungrouped irons.</li>
            </ul>
        </li>
        <li><b>Stony-Iron Meteorites:</b>
            <ul>
                <li>Mesosiderites (MES) and Pallasites (PAL), with subgroups like Eagle station pallasite (ES PAL).</li>
            </ul>
        </li>
    </ul>
</div>
""", unsafe_allow_html=True)

    st.image(classification_image_path, use_column_width=True)
    st.markdown(
        '<div style="text-align: center;">Classification of meteorites, more information on <a href="https://www.sciencedirect.com/science/article/pii/S0032063301000265">Classification</a></div>',
        unsafe_allow_html=True
    )

    st.markdown("""
    The following code defines a function that categorizes the various meteorite types listed in the 'reclass' column into broader family groups. It then applies this classification function to create a new column in the dataset, assigning each meteorite to its respective family group.
    """)
    st.image(count, caption="Counts for each classification group", use_column_width=False)

    st.markdown("""
    <div class="static-visualization">
    <b>Static visualization</b><br><br>
    Let's first run all the data (even the one that is wrong and not filtered) on a 2D static and non-interactive map in order to see how the data displays and if there is anything wrong or suspect.
    </div>
    """, unsafe_allow_html=True)


    st.image(Staticmap, caption="Static visualisation of the whole set", use_column_width=False)

    st.image(StaticHeatMap, caption="Static Heat Map", use_column_width=True)

    st.markdown("""
    <div class="outliers-analysis">
    <b>By definition latitude is bounded in degrees within the range [-90, 90] and longitude is bounded in degrees within the range [-180, 180)]. On the map it is clearly noticeable that there is some outlier data, which can be due to various reasons such as mistakes or data processing issues. We need to get rid of these values.</b><br><br>
    Number of outliers in latitude: 0<br>
    Number of outliers in longitude: 1<br>
    Total number of outliers: 1<br><br>
    <table>
    Outliers found :
        <tr><th>name</th><th>id</th><th>nametype</th><th>recclass</th><th>mass (g)</th><th>fall</th><th>year</th><th>reclat</th><th>reclong</th><th>GeoLocation</th><th>classification_group</th></tr>
        <tr><td>Meridiani Planum</td><td>32789</td><td>Valid</td><td>Iron, IAB complex</td><td>NaN</td><td>Found</td><td>2005.0</td><td>-1.94617</td><td>354.47333</td><td>(-1.94617, 354.47333)</td><td>IR</td></tr>
    </table>
    </div>
    """, unsafe_allow_html=True)

    st.image(mix, caption="Both maps after cleaning", use_column_width=True)


    st.markdown("""
    <div class="cleaning-success">
    The cleaning has been successfully done, represented by the new cleaned displays.
    </div>
    """, unsafe_allow_html=True)

    # Add next module text
    st.markdown("""
    <div class="next-module">
    The next module extends our meteorite data visualization by incorporating a color-coded classification system, allowing for the immediate identification of different meteorite types on a 2D map. An accompanying interactive HTML file provides a legend and detailed explanations of the color codes, enhancing the educational and analytical utility of the visualization. This upgrade facilitates a more nuanced exploration of the spatial distribution of meteorite landings globally.
    </div>
    """, unsafe_allow_html=True)

    st.image(Landing_by_classification_HTML, caption="Classification with and HTML", use_column_width=True)


    data_file = st.sidebar.file_uploader("Upload your meteorite landings data CSV", type=['csv'])
    selection_mode = st.sidebar.radio("Select data mode:", ("Random Sample", "Manual Selection"), key="selection_mode")

    if data_file is not None:
        data = load_data(data_file)

        # Check if the selection mode, file, or sample size has changed
        if (st.session_state.last_selection_mode != selection_mode or st.session_state.last_uploaded_file != data_file):
            st.session_state.data_sample = None
            st.session_state.last_selection_mode = selection_mode
            st.session_state.last_uploaded_file = data_file

        if selection_mode == "Random Sample":
            sample_size = st.sidebar.number_input("Sample Size", min_value=100, max_value=45000, value=st.session_state.last_sample_size, key="sample_size_input")
            # Update the last sample size in the session state
            if sample_size != st.session_state.last_sample_size:
                st.session_state.last_sample_size = sample_size
                st.session_state.data_sample = None  # Invalidate the current sample to force resampling

            if st.session_state.data_sample is None:
                df_filtered = data.dropna(subset=['reclat', 'reclong'])
                df_filtered = df_filtered[(df_filtered['reclat'] != 0) | (df_filtered['reclong'] != 0)]
                df_filtered['year'] = df_filtered['year'].fillna(0).astype(int)
                df_filtered = df_filtered[(df_filtered['reclat'] >= -90) & (df_filtered['reclat'] <= 90) &
                                          (df_filtered['reclong'] >= -180) & (df_filtered['reclong'] <= 180)]

                st.session_state.data_sample = df_filtered.sample(n=min(sample_size, len(df_filtered)), random_state=None)

            df_sampled = st.session_state.data_sample
        else:
            meteorite_names = st.sidebar.text_area("Enter meteorite names (comma-separated):", key="meteorite_names_input")
            if st.session_state.last_uploaded_file != data_file or st.session_state.last_selection_mode != selection_mode or meteorite_names != st.session_state.last_meteorite_names:
                st.session_state.last_uploaded_file = data_file
                st.session_state.last_selection_mode = selection_mode
                st.session_state.last_meteorite_names = meteorite_names

                meteorite_list = [name.strip() for name in meteorite_names.split(',')]
                if meteorite_list:
                    st.session_state.data_sample = data[data['name'].isin(meteorite_list)]
                else:
                    st.session_state.data_sample = pd.DataFrame()  # Empty DataFrame if no names are provided

            df_sampled = st.session_state.data_sample

        if df_sampled is not None and not df_sampled.empty:
            df_sampled['classification_group'] = df_sampled['recclass'].apply(classify_meteorites)
            cleaner = Cleaner(df_sampled)
            cleaned_data = cleaner.clean_data()

            tab1, tab2, tab3, tab4 = st.tabs(["Heatmap", "Meteorite Map", "Colour Points", "Input Map"])

            with tab1:
                st.write("For the Heat Map, we import cleaning modules as previously demonstrated. Once completed, the first code uses all the data to display a Heat Map. The code is set to zoom_start=2, which shows the entire map, but this causes the heat to be highly concentrated. To explore this map effectively, you need to zoom in on the desired location.")
                m = folium.Map(location=[0, 0], zoom_start=2)
                heat_data = cleaned_data[['reclat', 'reclong']].dropna().values.tolist()
                HeatMap(heat_data, radius=15).add_to(m)
                st_folium(m, width=1000, height=700)

            with tab2:
                st.write("This display is the first step in building the model. In this code, we present all the data in clusters. Running the code without clustering is not recommended, as it is resource-intensive to display every single point. The clusters in this code are dynamic and interactive, meaning they will subdivide and become smaller as you zoom in on the map. Clicking on a (blue) point reveals the exact location of a meteorite landing site. Pressing on these points will display detailed information about them.")
                meteorite_map = generate_meteorite_map(cleaned_data)
                st_folium(meteorite_map, width=1000, height=700)

            with tab3:
                st.write("This map advances our mapping capabilities by allowing us to change the marker colors based on the classification we applied. It retains all the features of the previous code. The module imported have all the libraries and cleaning function needed. ")
                meteorite_map_colour = create_map_colour(cleaned_data)
                st_folium(meteorite_map_colour, width=1000, height=700)

            with tab4:
                st.write("Based on previous tests and maps, the input function has proven to be the most effective. Therefore, we are reusing the same code with an additional step. The streamlit and streamlit_folium libraries allow users to draw on maps. This feature is particularly useful for calculating distances between points or marking important locations.")

                st.write("Now that we have a solid foundation for the final map, we can reuse the modules and code to make them work on Streamlit, with some necessary adaptations and additional features.")
                Map_with_input = create_map_with_input(cleaned_data)
                st_folium(Map_with_input, width=1000, height=700)

        else:
            st.error("No valid data available after filtering.")
    else:
        st.info("Please upload a CSV file to get started.")

if __name__ == "__main__":
    main()
