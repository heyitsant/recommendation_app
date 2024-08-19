import csv
import os
import re

#os.chdir(r'D:\OneDrive\Code\Python\Portfolio Projects\recommendation_app')

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
    return genres

def book_info(input):
    with open(input, encoding="utf-8") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter = ',')
        books = []
        for row in csv_reader:
            new_genres = ""
            for letter in row[3]:
                if letter in("[", "]", "'"):
                    continue
                else:
                    new_genres += letter
            #print(new_genres)
            #genre = [item for item in row[3].split(", ") if item is not "[" or "]"]#re.search('\[(.*)\]', row[3])
            #values = genre.group(1)
            books.append([row[1], row[0], row[2], row[4], new_genres.split(", ")])
            #print(row[1]) # Author
            #print(row[0]) # Title
            #print(row[2]) # Description
            #print(row[4]) # Rating
    #print(books)
    return(books)

book_info('goodreads_data.csv')

with open('books.py', 'w', encoding="utf-8") as b:
            b.write("genres = " + str(find_string('goodreads_data.csv', 3)) + '\n\n' + "books = " + str(book_info('goodreads_data.csv')))