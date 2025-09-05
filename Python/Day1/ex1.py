
firstname = "Virve"
print(firstname)

lastname = "Kask"
print(lastname)

fullname = firstname + " " + lastname
print(fullname)

full_name_upper = fullname.upper()
print(full_name_upper)

age = 30 
height = 1.60 

print("My name is " + fullname + ", I am " + str(age) + " years old and " + str(height) + " meters tall.")


print(f"Mu vanus on {age} ja pikkus on {height}.")

print(lastname[1])


hashed_name = lastname[0] + (len(lastname)-1) * firstname[0].lower()
print(hashed_name)

initials = firstname[0] + lastname[0]
print(initials)


