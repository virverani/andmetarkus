import pandas as pd 

# Create dataframe for electricity
df_electricity = pd.read_json('el_data_2025.json')
df_electricity = pd.json_normalize(df_electricity["data"])
df_electricity['timestamp'] = pd.to_datetime(df_electricity['datetime'])

print(df_electricity)
print(df_electricity.dtypes)

# Create dataframe for weather
df_weather = pd.read_csv('weather_2025.csv')
# Convert timestamp column to datetime
df_weather["timestamp"] = pd.to_datetime(df_weather["timestamp"])

print(df_weather)
print(df_weather.dtypes)

# Join two dataframes into one for analysis
df_merged = pd.merge(df_electricity, df_weather, left_on='timestamp', right_on='timestamp')
print(df_merged)

# Create visual for price, wind and temperature
import matplotlib.pyplot as plt

sorted_data = df_merged.sort_values("timestamp")

# Base figure
fig, ax1 = plt.subplots(figsize=(10, 5))

# Plot TA on ax1
ax1.plot(sorted_data["timestamp"], sorted_data["TA"], color="tab:blue", label="TA")
ax1.set_ylabel("TA (°C)", color="tab:blue")
ax1.tick_params(axis="y", labelcolor="tab:blue")

# Create second y-axis for WSX1H
ax2 = ax1.twinx()
ax2.plot(sorted_data["timestamp"], sorted_data["WSX1H"], color="tab:green", label="WSX1H")
ax2.set_ylabel("WSX1H (m/s)", color="tab:green")
ax2.tick_params(axis="y", labelcolor="tab:green")

# Create third y-axis for price
ax3 = ax1.twinx()
ax3.spines['right'].set_position(('outward', 60))  # offset third axis
ax3.plot(sorted_data["timestamp"], sorted_data["price"], color="tab:red", label="Price")
ax3.set_ylabel("Price (€/MWh)", color="tab:red")
ax3.tick_params(axis="y", labelcolor="tab:red")

# Optional: improve layout
fig.tight_layout()
plt.show()


# Calculate correlation 
correlation_matrix = df_merged[['price', 'WSX1H', 'TA']].corr()
print(correlation_matrix)

