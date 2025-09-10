# Ilma ja linna andmete analüüs

import pandas as pd

ilmaandmed = {
    "linn": ["Tallinn", "Tartu", "Pärnu", "Narva", "Kuressaare"],
    "temperatuur": [18.5, 19.2, 17.8, 16.4, 15.9],
    "niiskus": [65, 60, 70, 68, 75],
    "tuul": [4.2, 3.8, 5.0, 4.5, 6.1]
}

linnad_andmed = {
    "linn": ["Tallinn", "Tartu", "Pärnu", "Narva", "Kuressaare"],
    "elanike_arv": [440000, 95000, 51000, 57000],
    "pindala": [159.2, 38.8, 32.2, 84.5, 15.0]  # km²
}

# Leia, millises linnas on kõrgeim temperatuur.

# Loo dataframe ilmale
df_ilm = pd.DataFrame(ilmaandmed)
print(df_ilm)

# Lisa Kuressaare rahvaarv
linnad_andmed1 = linnad_andmed

# Leia Kuressaare koht listis
index = linnad_andmed1['linn'].index('Kuressaare')

# Tee piisava pikkusega list
while len(linnad_andmed1['elanike_arv']) <= index:
    linnad_andmed1['elanike_arv'].append(None)

# Lisa Kuressaarele elanike arv
linnad_andmed1['elanike_arv'][index] = 13000

print(linnad_andmed1)

# Loo linnade dataframe
df_linnad = pd.DataFrame(linnad_andmed1)
print(df_linnad)

# Seo tabelid kokku 
merged_data = pd.merge(df_ilm, df_linnad, on = 'linn')
print(merged_data)

# Leia, millises linnas on kõrgeim temperatuur
korgeim_temp = merged_data['temperatuur'].max()
korgeim_temp_rida = merged_data.loc[merged_data["temperatuur"] == korgeim_temp]

print(korgeim_temp_rida)

# Arvuta iga linna rahvastikutihedus (elanike arv / pindala).
merged_data["rahvastikutihedus"] = (
round(merged_data['elanike_arv']/merged_data["pindala"])
)

print(merged_data)

# Filtreeri välja linnad, kus niiskus on üle 70%.
linnad_niiskus_ule_70 = merged_data.loc[merged_data["niiskus"] > 70]
print(linnad_niiskus_ule_70)

# Sorteeri andmed tuule kiiruse järgi kasvavalt.
linnad_sorteeritud_tuule_kiirus = merged_data.sort_values(by='tuul')
print (linnad_sorteeritud_tuule_kiirus)

# Lisa uus veerg, mis näitab kas temperatuur 
# on üle keskmise ("üle keskmise" / "alla keskmise").
avg_temp = merged_data["temperatuur"].mean()

linnad_keskmine_temp = merged_data

linnad_keskmine_temp.loc[linnad_keskmine_temp["temperatuur"] > avg_temp, 'keskmine_vordlus'] = "üle keskmise"
linnad_keskmine_temp.loc[linnad_keskmine_temp["temperatuur"] <= avg_temp, 'keskmine_vordlus'] = "alla keskmise"

print(linnad_keskmine_temp)

# Leia, millises linnas on kõige rohkem elanikke.
max_pop = merged_data["elanike_arv"].max()
max_population_row = merged_data.loc[merged_data["elanike_arv"] == max_pop]
print(max_population_row)

# Asenda kõik linnanimed suurte tähtedega.
linn_suured_tahed = merged_data
linn_suured_tahed['linn'] = merged_data["linn"].str.upper()
print(linn_suured_tahed)

# Salvesta lõplik DataFrame CSV-failina.
merged_data.to_csv('linnad.csv')