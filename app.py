# Book recommendation application.
# Choose fiction or non-fiction. These will be separate libraries. - Nice to have
# Choose a genre. - Must have
# Choose length of book. - Nice to have
# Choose if book is standalone or part of a series - Nice to have

from linkedlist import List


linked_list = List()
linked_list.insert_beginning("Antony")

print(linked_list.stringify_list())

linked_list.insert_beginning("Liz")
linked_list.insert_beginning("Chloe")

print(linked_list.stringify_list())