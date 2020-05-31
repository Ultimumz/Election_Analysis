# Add our dependencies.
import csv
import os

# Assign a variable for the file to load and the path.
file_to_load = os.path.join('Resources', 'election_results.csv')

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file
with open(file_to_load) as election_data:

    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    # Print each row in the CSV file.
    #for row in file_reader:
        #print(row)
    
    # Print the header row.
    headers = next(file_reader)
    print(headers)

# Using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:

    # Write some data to the file.
    #txt_file.write("Hello World")

    # Write three counties to the file.
    txt_file.write("Counties in the Election\n-------------------------\n")
    txt_file.write("Arapahoe\nDenver\nJefferson")

# Close the file.
election_data.close()