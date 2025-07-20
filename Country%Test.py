# coding: utf-8
import pandas as pd
df = pd.read_csv(r"C:\country_level_data.csv")
print(df['country_name'])

import streamlit as st
import plotly.express as px
import geopandas as gpd
st.title('Country Level Data')
world = gpd.read_file(r"C:\Users\ChrisPuduski\ne_110m_admin_0_countries\ne_110m_admin_0_countries.shp")
fig = px.choropleth(world, geojson=world.geometry, locations=world.index, color=world['CONTINENT'], hover_name=world['NAME'], projection="natural earth")

fig.update_geos(fitbounds="locations", visible=False)
st.plotly_chart(fig, use_container_width=True)

get_ipython().run_line_magic('save', 'Country%Test.py 1-20')
st.write("This is a simple Streamlit app that displays country-level data on a map.")
