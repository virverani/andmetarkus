# Import data from worldbank about populations

import requests
import json 
import pandas as pd 
import matplotlib.pyplot as plt 

# Take data from urls
url_country = "https://api.worldbank.org/v2/country/ee?format=json"
url_population = "https://api.worldbank.org/v2/country/EST/indicator/SP.POP.TOTL?format=json"

response = requests.get(url_population)
data = response.json()

values = {'year': [], 'population': []}

for item in data[1]:
    values['year'].append(item['date'])
    values['population'].append(item['value'])

df = pd.DataFrame(values)
df = df.sort_values('year', ascending=True)

print(df)

# Create a line graph 
df.plot(x= 'year', y= 'population', ylim= 0, kind='line', marker='o', 
        title = 'Estonian population', xlabel = 'Year', ylabel='Population'
        )

plt.ylim(top = df['population'].max()+100000)

# Save graph file 
plt.savefig('EE_population.png')
plt.show()


# Create a bar graph 
df.plot(x= 'year', y= 'population', ylim= 0, kind='bar',
        title = 'Estonian population', xlabel = 'Year', ylabel='Population'
        )

plt.ylim(top = df['population'].max()+100000)

plt.savefig('EE_population_bar.png')
plt.show()