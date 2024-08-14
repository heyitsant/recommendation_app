from node import Node

class List():
    def __init__(self, head_node=None):
        self.head_node = head_node

    def get_head_node(self):
        return self.head_node
    
    def insert_beginning(self, new_value):
        new_node = Node(new_value)
        new_node.set_next_node(self.head_node)
        self.head_node = new_node

    def stringify_list(self):
        string_list = ""
        current_node = self.head_node
        while current_node:
            string_list += str(current_node.value) + "\n"
            current_node = current_node.get_next_node()
        return string_list
