# Book recommendation application.
# Choose fiction or non-fiction. These will be separate libraries. - Nice to have
# Choose a genre. - Must have
# Choose length of book. - Nice to have
# Choose if book is standalone or part of a series - Nice to have

from linkedlist import *
from books import *


def genre_list():
    book_genres = List()
    for genre in genres:
        book_genres.insert_beginning(genre)
    return book_genres

def book_data():
    book_data_list = List()
    for genre in genres:
        book_sublist = List()
        for book in books:
            for book_genre in book[4]:
                if book_genre == genre:
                    book_sublist.insert_beginning(book)
                continue
            continue
        book_data_list.insert_beginning(book_sublist)
    return book_data_list

my_book_genres = genre_list()
my_book_list = book_data()

selected_genre = ""

while len(selected_genre) == 0:
    user_input = str(input(
        "\nWhat type of book would you like to read?\nType the first few letters of the genre to see if it's here.\n"
    )).lower()

    matching_types = []
    type_list_head = my_book_genres.get_head_node()
    while type_list_head is not None:
        if str(type_list_head.get_value()).startswith(user_input):
            matching_types.append(type_list_head.get_value())
        type_list_head = type_list_head.get_next_node()

    for genre in matching_types:
        print(genre)