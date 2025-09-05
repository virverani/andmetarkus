# Assign an age to a variable.
age = 18
print(age)


# Check the age and see if a person if the person can vote.
if age >= 18: 
    print("You can vote in national elections.") 
if age >= 16: 
    print("You can vote in local elections.")
else: 
    print("You can't vote yet.")

# Number to be checked. 
num = 98
print(num)

# Check if number is bigger than 100. 
if num > 100: 
    print("The number is greater than 100.")
if num == 100: 
        print("The number is 100.")
if num < 100: 
    print("The number is less than 100.")

# Same comparison using elif.
if num > 100: 
    print("The number is greater than 100.")
elif num == 100: 
    print("The number is 100.")
else:
    print("The number is less than 100.")