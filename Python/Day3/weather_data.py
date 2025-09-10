import requests
import json
import pandas as pd

url = "https://keskkonnaandmed.envir.ee/f_kliima_tund?aasta=eq.2025&jaam_nimi=eq.Tallinn-Harku&element_kood=in.(TA,WSX1H)"
response = requests.get(url)
data = response.json()



df = pd.DataFrame(data)

new_df = df[["jaam_nimi", "element_kood", "element_yhik_eng", "vaartus", "aasta", "kuu", "paev", "tund"]]

# Rename date columns so they can be used in datetime function
df_renamed = new_df.rename(columns={
    "aasta": "year",
    "kuu": "month",
    "paev": "day",
    "tund": "hour"
})

# Create datetime as a timestamp column
df_renamed["timestamp"] = pd.to_datetime(df_renamed[["year", "month", "day", "hour"]])

print(df_renamed)

# Put wind and temperature into separate columns
df_wide = df_renamed.pivot(index="timestamp", columns="element_kood", values="vaartus").reset_index()
print(df_wide)

# Save to CSV file
df_wide.to_csv("weather_2025.csv", index=False)


