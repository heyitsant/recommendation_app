import csv
import os

os.chdir(r'D:\OneDrive\Code\Python\Portfolio Projects\recommendation_app')

def find_string(input, column_number):
    # Function to find and separate words in long string.
    # This function will return a dictionary of unique terms found in specified column, as a Python dictionary
    
    with open(input, encoding="utf-8") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter = ',')
        genres = []
        
        for row in csv_reader:
            if len(row[column_number]) <= 2:
                continue
            else:
                list = row[3].split("', '")
                for item in list:
                    if item not in genres:
                        genres.append(item)
        
        # This is a dirty bit of code to clean up any further undesireable characters.
        idx = 0
        for item in genres:
            for char in item:
                if char in " ['']":
                    genres[idx] = item.replace(char,'')
                    item = item.replace(char,'')  
            idx += 1

def book_info(input):
    with open(input, encoding="utf-8") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter = ',')
        for row in csv_reader:
            print("Author: " + row[1])
            print("Title: " + row[0])
            print("Description: " + row[2])
            print("Rating: " + row[4])

book_info('goodreads_data.csv')