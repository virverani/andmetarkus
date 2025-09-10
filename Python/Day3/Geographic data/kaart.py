"""
Eesti maakondade choropleth (elanike arv) Plotly + GeoPandas abil.

Eeldused:
  pip install geopandas plotly
  pip install kaleido  # piltide salvestamiseks (vajadusel)
"""
import plotly.graph_objects as go
import pandas as pd
import geopandas as gpd
import os


GEOJSON_PATH = "EST_adm1.geojson"

if not os.path.exists(GEOJSON_PATH):
    raise FileNotFoundError(
        f"Puudub {GEOJSON_PATH}. Lae Eesti maakondade geoandmed (adm1) ja salvesta samasse kausta."
    )

# Lae geoandmed (maakonnad / admin tasemel 1)
estonia = gpd.read_file(GEOJSON_PATH)

# Kontrolli olemasolevat nimeveeru (GADM versiooniti võib olla NAME_1)
name_col = None
for cand in ["NAME_1", "NAME_ENG", "name", "NAME"]:
    if cand in estonia.columns:
        name_col = cand
        break
if not name_col:
    raise ValueError(
        "Ei leidnud maakonna nime veergu (NAME_1 / NAME_ENG / name).")

estonia["maakond"] = estonia[name_col]

# Näidisandmed (asenda päris andmetega vajadusel)
population_data = pd.DataFrame({
    "maakond": [
        "Harju", "Hiiu", "Ida-Viru", "Jõgeva", "Järva", "Lääne",
        "Lääne-Viru", "Põlva", "Pärnu", "Rapla", "Saare",
        "Tartu", "Valga", "Viljandi", "Võru"
    ],
    "elanike_arv": [
        605000, 9000, 135000, 28000, 30000, 23000,
        58000, 28000, 84000, 33000, 31000,
        150000, 28000, 48000, 35000
    ]
})

# Ühenda
gdf = estonia.merge(population_data, on="maakond", how="left")

# GeoJSON struktuur Plotly jaoks
geojson_obj = gdf.__geo_interface__

fig = go.Figure(go.Choroplethmapbox(
    geojson=geojson_obj,
    locations=gdf["maakond"],
    z=gdf["elanike_arv"],
    featureidkey="properties.maakond",
    colorscale="Viridis",
    marker_opacity=0.75,
    marker_line_width=0.8,
    colorbar_title="Elanike arv"
))

fig.update_layout(
    mapbox_style="carto-positron",
    mapbox_zoom=6,
    mapbox_center={"lat": 58.7, "lon": 25.3},
    margin={"r": 0, "t": 40, "l": 0, "b": 0},
    title="Eesti maakonnad – näidis elanike arv"
)

# Kommenteeri allolevad rea tagasi, kui kasutad Jupyterit
# import plotly.io as pio
# pio.renderers.default = "notebook"

fig.show()

# salvesta HTML faili
fig.write_html("kaart_tulemus.html")
print("Graafik salvestati faili kaart/kaart_tulemus.html – ava see brauseris.")

# salvesta pildina (vajab kaleido)
fig.write_image("kaart_tulemus.png")
print("Graafik salvestati faili kaart/kaart_tulemus.png")