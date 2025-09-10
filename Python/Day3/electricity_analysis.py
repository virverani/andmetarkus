#Create dataframe for the 2025 data 

import pandas as pd 

df = pd.read_json('el_data_2025.json')

df_expanded = pd.json_normalize(df["data"])

df_expanded.head()

# Create a visual of electricity price
import matplotlib.pyplot as plt

df_expanded.plot(x='datetime', y='price', kind= 'line', title = 'EE electricity prices')

plt.show()

# Create a visual of electricity price for 2025-08-01
df_expanded["datetime"] = pd.to_datetime(df_expanded["datetime"])

filtered = df_expanded[df_expanded["datetime"].dt.date == pd.to_datetime("2025-08-01").date()]
print(filtered)

filtered = filtered.sort_values("datetime")

filtered.plot(x='datetime', y='price', kind= 'line', marker = 'o'
              , title = 'EE electricity prices 01.08.2025')

plt.show()