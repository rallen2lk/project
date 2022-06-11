import pandas as pd
import streamlit as st
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import requests
import folium
import geopandas as gpd
import re
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
import streamlit_folium
from streamlit_folium import st_folium


s = pd.read_csv('check.csv')
st.write(s)

l = pd.read_csv('data.csv')

gdf = gpd.GeoDataFrame(l, geometry=gpd.points_from_xy(l['lon'], l['lat']))
st.write(gdf)

m = folium.Map([55.75364, 37.648280], zoom_start=10)
for ind, row in gdf.iterrows():
    folium.Marker([row.lat, row.lon], radius=30, fill_color='red').add_to(m)

a=st_folium(m)

lol = pd.read_csv('moscow.csv')
l = gpd.GeoDataFrame(wil, geometry = gpd.points_from_xy(l['lon'], l['lat']))
gl = l.sjoin(lol, how="inner", predicate='intersects')
st.write(gl)
