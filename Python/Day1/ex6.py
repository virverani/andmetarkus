# Use list compherension
# Create a list of girl names
girl_names = ("Jaanika", "Malle", "Kersti", "Ann", "Mari", "Kati")

# Just check for capitalized letter
print("\nNames starting with M:")
names_starting_with_m = [name for name in girl_names if "M" in name]
print(names_starting_with_m)

# Check the first letter
print("\nNames starting with A:")
names_starting_with_a = [name for name in girl_names if "A" in name[0]]
print(names_starting_with_a)

# Check the first letter with startswith command
print("\nNames starting with A:")
names_starting_with_a = [name for name in girl_names if name.startswith("A")]
print(names_starting_with_a)

# Names that are shorter than 5 letters
print("\nNames shorter than 5 letters:")
names_shorter_than_5 = [name for name in girl_names if len(name) < 5]
print(names_shorter_than_5)
