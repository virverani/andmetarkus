# Andmete laadimine veebilehelt
# Reisibüroo reiside hinnad

import requests
from bs4 import BeautifulSoup

link = "https://www.reisiekspert.ee/et/reiside-eripakkumised/55-egiptus"

response = requests.get(link)
soup = BeautifulSoup(response.text, "html.parser")


reisi_kaart = soup.find_all("div", class_="card-body")
# hinnad = soup.find_all("span", class_="promohind_realopus")
# reisinimed = soup.find_all("span", class_="promohind_realopus")

for reis in reisi_kaart:
    reisi_nimi = reis.find("h2").text.strip()
    hind_span = reis.find("span", class_="promohind_realopus")
    if hind_span is None:
        continue
    reisi_hind = hind_span.text.strip().replace("€", "").replace("\n ", "").replace('\xa0', '').strip()

    reisi_andmed = reisi_nimi, reisi_hind

    print(reisi_andmed)


