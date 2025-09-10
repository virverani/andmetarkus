# Esimene tekst
sonad = ["    õun", "banaan    ", "    pirn    ", "ploom", "    viinamari    "]

# Eemalda tühikud - strip käsk
sonad_tuhikuteta_strip = []
for sona in sonad:
    sonad_tuhikuteta_strip.append(sona.strip())

print(sonad_tuhikuteta_strip)

# Eemalda tühikud - replace käsk
sonad_tuhikuteta_replace = []
for sona in sonad:
    sonad_tuhikuteta_replace.append(sona.replace(" ", ""))

print(sonad_tuhikuteta_replace)

# Teine tekst - numbrilised väärtused
summad = ["1,234.56", "12,000.00", "5,678.90", "100.00", "23,456.78"]

# Moodusta uus järjend, kus sõne on teisendatud ujukomaarvuks (float)
summad_float = []
for summa in summad:
    summa = summa.replace(",", "")
    summad_float.append(float(summa))

print(summad_float)
print(sum(summad_float))