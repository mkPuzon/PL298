'''
Reads headers into txt file.
'''
import csv

# Open the CSV file
with open('hhpub23.csv', newline='') as csvfile:
    # Create a CSV reader object
    csv_reader = csv.reader(csvfile)
    
    # Read the first row of the CSV file
    first_row = next(csv_reader)
    
    with open('hhpub_key.txt', 'w') as txtfile:
        # Write each element along with its index to the text file
        for index, element in enumerate(first_row):
            txtfile.write(f"{index}: {element} == \n")
