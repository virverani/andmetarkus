# Read data from Excel 
import pandas as pd 

loaded_data = pd.read_excel ('input/ProductTable.xlsx')

print("\nData from Excel:")
print (loaded_data)

# Data to dictionaries
data_dict = loaded_data.to_dict(orient = 'records')
print("\nData from Excel as dictionary:")
print(data_dict)