
# Create a function which checks if a person is an adult.
def is_adult(age):
    """Check if age is 18 or more.""" # Adds description to the function.
    if age >= 18: 
        return True
    else:   
        return False

# Check if 21 is an adult.
print(is_adult(21))

# Check if 15 is an adult.
print(is_adult(15))

# Create a function which checks if the entered number is number.
def is_adult(age):
    if not isinstance(age, int):
        return "Please enter a number."
    if age < 0: 
        return "Age can't be negative."
    if age >= 18: 
        return True
    else:   
        return False

# Check if "Mari" is a valid age.
print(is_adult("Mari"))

# Check if -21 is a valid age and if it is an adult.
print(is_adult(-21))

# Check if 21 is a valid age and if it is an adult.
print(is_adult(21))


# Create a list of EU northern countries.
eu_northeren_countries = ["DK", "FI", "IS", "NO", "SE"]

# Create a function to check if a value is in a list.
def is_eu_northeren_countries(country_code):
    if country_code in eu_northeren_countries:
        return True
    else: return False

# Check if FI is in the list.    
print (is_eu_northeren_countries("FI"))

# Check if EE is in the list.
print (is_eu_northeren_countries("EE"))

