import glob
import json

# Create dataframe for 2025 data
el_data=[]


for filename in glob.glob("*.json"):
    if "2025" in filename: 
        with open(filename, "r", encoding="utf-8") as f:
            data  = json.load(f)
            el_data += data['data']

# Save it as a json file
with open("el_data_2025.json", "w", encoding="utf-8") as f:
    json.dump({"data": el_data}, f, ensure_ascii=False, indent=2)
print("Andmed salvestatud faili el_data_2025.json")
            

