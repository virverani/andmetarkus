# Import necessary libraries
import geopandas as gpd
import matplotlib.pyplot as plt
import pandas as pd 
import seaborn as sb 
import requests

# Get weather data
url = 'https://www.ilmateenistus.ee/ilma_andmed/xml/forecast.php'

response = requests.get(url)
xml_content = response.content

df = pd.read_xml(xml_content, xpath=".//place")

print(df.head())

