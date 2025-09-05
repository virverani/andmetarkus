# For cycle

# Create a list of girl names
girl_names = ("Jaanika", "Malle", "Kersti", "Ann", "Mari", "Kati")

# Return each name as a new row
for name in girl_names: 
     print(name)

# Return first two names with range keyword
for i in range(2):
     print(girl_names[i])

# Return first two names with specifying the range in list
for name in girl_names[:2]:
    print(name)

# Return second to fourth name 
for name in girl_names[1:4]:
    print(name)


# Return names in reversed order compared to original list
print("Reversed order:")
for name in reversed(girl_names):
     print(name)

# Return names starting with K
print("\nNames starting with K:")

for name in girl_names:
    if name[0] == "K":
        print (name)

# Create a dictionary that has the names starting with M

print("\nNames starting with M:")
names_starting_with_M = {"M": []}
names_starting_with_M = []
for name in girl_names:
        if name[0] == "M":
         names_starting_with_M.append(name)

print(names_starting_with_M)

