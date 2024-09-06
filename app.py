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

#print(my_book_genres.stringify_list())

selected_genre = ""

while len(selected_genre) == 0:
    user_input = str(input(
        "\nWhat type of book would you like to read?\nType the first few letters of the genre to see if it's here.\n"
    )).lower()

    matching_types = []
    type_list_head = my_book_genres.get_head_node()
    while type_list_head is not None:
        if str(type_list_head.get_value()).lower().startswith(user_input):
            if str(type_list_head.get_value()) not in matching_types:
                matching_types.append(type_list_head.get_value())
        type_list_head = type_list_head.get_next_node()
    print("\n")
    for genre in matching_types:
        print(genre)

    if len(matching_types) == 1:
        select_genre = str(input("\n" + matching_types[0] +" is the only matching genre for your choice.\nDo you want to see the books that match this genre?\nEnter y for yes or n for no\n")).lower()

        if select_genre == "y":
            selected_genre = matching_types[0]
            print("Selected genre: " + selected_genre)
            book_list_head = my_book_list.get_head_node()
            while book_list_head.get_next_node() is not None:
                sublist_head = book_list_head.get_value().get_head_node()
                print(sublist_head.value)

