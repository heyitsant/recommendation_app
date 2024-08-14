import csv
import os

os.chdir(r'D:\OneDrive\Code\Python\Portfolio Projects\recommendation_app')

def find_string(input, column_number):
    # Function to find and separate words in long string.
    # This function will return a dictionary of unique terms found in specified column, as a Python dictionary
    
    with open(input, encoding="utf-8") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter = ',')
        genres = []
        word = ""
        
        for row in csv_reader:
            if len(row[column_number]) <= 2:
                continue
            else:
                #print(row[3])
                list = row[3].split("', '")
                for item in list:
                    if item not in genres:
                        genres.append(item)
        idx = 0
        for item in genres:
            for char in item:
                if char in " ['']":
                    genres[idx] = item.replace(char,'')
                    item = item.replace(char,'')  
            idx += 1
        print(genres)

find_string('goodreads_data.csv', 3)