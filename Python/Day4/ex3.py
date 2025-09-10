import re

text = "Tere!   (Kas sa tuled?)  Ma ei tea...võib-olla,   aga -- vaatame!  Õhtul, kell 18:00, \"Kohvikus\"."

# Eemalda liigsed tühikud (asenda mitu tühikut ühega)
text = re.sub(r'\s+', ' ', text).strip()

print(text)
# väljund: Tere! (Kas sa tuled?) Ma ei tea...võib-olla, aga -- vaatame! Õhtul, kell 18:00, \"Kohvikus\"."

# Eemalda kõik sulud ja nende sees olev tekst - substitute käsk
text = re.sub(r'\(.*?\)', '', text)

print(text)

# Eemalda jutumärgid ja -- - replace funktsionaalsus, saab mitu replacei üksteise otsa panna
text = text.replace('"', "").replace("-- ", "")

print(text)