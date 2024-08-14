import csv

def find_string(input, column_number):
    # Function to find and separate words in long string.
    # This function will return a dictionary of unique terms found in specified column, as a Python dictionary
    
    with open(input, encoding="utf-8") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter = ',')
        genres = []
        word = ""
        for row in csv_reader:
            print(row[column_number])


find_string('goodreads_data.csv', 3)