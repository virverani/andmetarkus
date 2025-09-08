# Read in a text file and print its content

def main():
    with open("ex1_source.txt", encoding='utf-8') as f:
        file_content = f.read()

    return file_content

print("\nText file contents:")
print(main())
    

# Read in a CSV file and print its content as a list
import csv 
with open ('C:/Users/virve/OneDrive - BCS AS/Documents/Andmetarkus/Python/Day2/input/CustomerTable.csv') as file:
    reader = csv.reader(file)
    data = list(reader)

    print("\nCSV file contents as a list:")
    print(data)


# Read in a CSV file and print its content as a text file
def open_csv(): 
    with open("input/CustomerTable.csv") as csv_file: 
        file_content = csv_file.read()

    return file_content

print("\nCSV file contents as a text file:")
print(open_csv())


# Call out a function from another file 
from file_functions import FileFunctions

# Use the function to add a line
def main():

    file_path = r"C:/Users/virve/OneDrive - BCS AS/Documents/Andmetarkus/Python/Day2/ex1_source.txt"

    request_log_entries = FileFunctions().read_file(file_path)

    for line in request_log_entries:
        print(line + "\n")

    row_count = len(request_log_entries)
    print(f"Logifailis on {row_count} rida.")

    FileFunctions().add_line_to_file(
        file_path, f"Logifailis on {row_count} rida.")

print(main())







