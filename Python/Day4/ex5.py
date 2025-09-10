
# Loo nimeline tervitus

nimed = ["Mari", "Jüri", "Kati"]
for nimi in nimed:
    print("Tere,", nimi + "!")

# Kirjuta for-tsükliga programm, mis leiab ja väljastab salvestab teise järjendisse kõik riigid, mis algavad kas E või A tähega.
riigid = ["Eesti", "Austria", "Belgia", "Andorra", "Hispaania", "Soome", "Albaania", "Itaalia"]

riigid_a_e = []
for riik in riigid: 
   if riik[0] in ('E', 'A'):
       riigid_a_e.append(riik)

print(riigid_a_e)

# Sõnastiku tüüpi andmete töötlemine
pealinnad = {
    "Eesti": "Tallinn",
    "Soome": "Helsingi",
    "Rootsi": "Stockholm"
}

for riik, linn in pealinnad.items():
    print(f"{riik} pealinn on {linn}.")


# Toidu koostisosad
toidud = {
    "õun": {
        "kalorsus": 52,
        "vitamiinid": ["C", "K", "B6"],
        "mineraalid": ["Kaalium", "Magneesium"],
        "süsivesikud": 14,
        "rasv": 0.2,
        "valk": 0.3
    },
    "banaan": {
        "kalorsus": 89,
        "vitamiinid": ["C", "B6"],
        "mineraalid": ["Kaalium", "Magneesium"],
        "süsivesikud": 23,
        "rasv": 0.3,
        "valk": 1.1
    },
    "kanafilee": {
        "kalorsus": 165,
        "vitamiinid": ["B3", "B6", "B12"],
        "mineraalid": ["Fosfor", "Seleen"],
        "süsivesikud": 0,
        "rasv": 3.6,
        "valk": 31.0
    },
    "kartul": {
        "kalorsus": 77,
        "vitamiinid": ["C", "B6"],
        "mineraalid": ["Kaalium", "Raud"],
        "süsivesikud": 17,
        "rasv": 0.1,
        "valk": 2.0
    },
    "lõhe": {
        "kalorsus": 208,
        "vitamiinid": ["D", "B12", "B6"],
        "mineraalid": ["Seleen", "Fosfor"],
        "süsivesikud": 0,
        "rasv": 13.0,
        "valk": 20.0
    },
    "riis": {
        "kalorsus": 130,
        "vitamiinid": ["B1", "B3", "B6"],
        "mineraalid": ["Magneesium", "Fosfor"],
        "süsivesikud": 28,
        "rasv": 0.3,
        "valk": 2.7
    }
}

for toit, info in toidud.items():
    print(f"{toit} mineraalid:", info["mineraalid"])


# Toidud, mille mineraalide hulgas on "Kaalium".
for toit, info in toidud.items():
        if "Kaalium" in info["mineraalid"] :
            print(toit, info["mineraalid"])


# Lisada lisatunnus "makro" väärtusega "süsivesikurohke", "rasvane" 
# kui vastav osakaal makrotoitainetest on üle 50%.
# Muudel juhtudel lisa tekst "mitmekülgne"

for toit, toiduomadused in toidud.items():
    kokku = toiduomadused["süsivesikud"] + toiduomadused["rasv"] + toiduomadused["valk"]  
    if toiduomadused["süsivesikud"]/kokku > 0.5: toiduomadused["makro"] = "süsivesikuterohke"
    elif toiduomadused["rasv"]/kokku > 0.5: toiduomadused["makro"] =  "rasvane"
    else: toiduomadused["makro"] = "mitmekülgne"

for toit, info in toidud.items():
    print(toit, info['makro'])


# Toidud, mille vitamiinide hulgas on vähemalt kaks B vitamiini 
# ja lisa need uude sõnastikku "b_vitamiini_rikas"

b_vitamiini_rikas = {}
for toit, toiduomadused in toidud.items():
    b_vitamiinide_arv = sum(
        1 for vit in toiduomadused["vitamiinid"] if vit.startswith("B"))
    if b_vitamiinide_arv >= 2:
        b_vitamiini_rikas[toit] = toiduomadused["vitamiinid"]

print(b_vitamiini_rikas)


# For tsüklitega sama lahendus
b_vitamiini_rikas2 = {}
for toit, toiduomadused in toidud.items():
    b_vitamiinide_arv = 0 
    for vit in toiduomadused["vitamiinid"]:
        if vit.startswith('B'):
            b_vitamiinide_arv +=1
        if b_vitamiinide_arv >= 2: 
            b_vitamiini_rikas2[toit] = toiduomadused["vitamiinid"]

print(b_vitamiini_rikas2)
