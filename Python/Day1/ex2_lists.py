# Creating a list
boys_names = ["Kusti", "Peeter", "Juku", "Mati", "Jaan"]
print (boys_names)
print (boys_names[0])

# Adding a new item to the list 
boys_names.append("Joonas")
print(boys_names)

# Creating a list
girl_names = ["Malle", "Kristi", "Mari", "Jaanika", "Maiu"]
print (girl_names)
print (girl_names[0])

# Adding a new item to the list 
girl_names.append("Marta")
print(girl_names)

# Create an empty list 
empty_list = []
print(empty_list)

# Add two lists together
names = boys_names + girl_names
print(names)

# Sort the list 
names_sorted = sorted(names)
print(names_sorted)

# Find alphabetically first and last name
print("Alphabetically first name is:", min(names_sorted))
print("Alphabetically last name is:", max(names_sorted))

# Find the number of names in the list
print("Number of names in the list is:", len(names_sorted))

# Find the first and last element of the list 
print("First name in the list is:", names_sorted[0])
print("Last name in the list is:", names_sorted[-1])

# Sort the list in reverse alphabetical order
names_sorted_reverse = sorted(names, reverse=True)
print(names_sorted_reverse)

# Sort the original list in alphabetical order
names.sort()
print(names)

# Sort the original list in reverse order
names.reverse()
print(names)