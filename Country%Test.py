# coding: utf-8
#import pandas as pd
#df = pd.read_csv(r"C:\country_level_data.csv")
#print(df['country_name'])

import zipfile
import tempfile
import os
import streamlit as st
import plotly.express as px
import geopandas as gpd

st.title('Country Level Data')

upload_zip = st.file_uploader(r"C:\Users\ChrisPuduski\ne_110m_admin_0_countries.zip", type=["zip"])

if upload_zip is not None:
    with tempfile.TemporaryDirectory() as tmpdirname:
        with zipfile.ZipFile(upload_zip, 'r') as zip_ref:
            zip_ref.extractall(tmpdirname)
        shapefile_path = os.path.join(tmpdirname, "ne_110m_admin_0_countries.shp")
        world = gpd.read_file(shapefile_path)
        fig = px.choropleth(world, geojson=world.geometry, locations=world.index, color=world['CONTINENT'], hover_name=world['NAME'], projection="natural earth")

        fig.update_geos(fitbounds="locations", visible=False)
        st.plotly_chart(fig, use_container_width=True)
else:
    st.info("Please upload a zip file containing the shapefile.")

get_ipython().run_line_magic('save', 'Country%Test.py 1-20')
st.write("This is a simple Streamlit app that displays country-level data on a map.")
