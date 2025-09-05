# Create a dictionary for my company data 
my_company_data = {"id":12345678, "name": "Firma ABC"}
print(my_company_data)

# Add sales data to the created dictionary
my_company_data["yearsales"] = {2023:10000, 2024:20000, 2025:30000}
print(my_company_data)

# Change company name
my_company_data["name"] = "Firma XYZ"
print(my_company_data)

# Add a new key-value pair for the company address
my_company_data["address"] = "Tallinn, Estonia"
print(my_company_data)

# Change sales number for the year 2025
my_company_data["yearsales"][2025] = 40000
print(my_company_data)

# Add sales for 2026 
my_company_data["yearsales"][2026] = 50000
print(my_company_data)