class Binary_tree:
    def __init__(self, size):
        self.custom_list = size * [None]
        self.last_used_index = 0
        self.max_size = size

    def insert_node(self, value):
        if self.last_used_index + 1 == self.max_size:
            return "The Binary tree is full"
        self.custom_list[self.last_used_index + 1] = value
        self.last_used_index +=1
        return "The value has been successfully inserted"

    def search_node(self, node_value):
        for i in range(len(self.custom_list)):
            if self.custom_list[i] == node_value:
                return "Node found"
        return "Node not found"


new_bt = Binary_tree(8)
new_bt.insert_node("Drinks")
new_bt.insert_node("Hot")
new_bt.insert_node("Cold")
print(new_bt.search_node("Cold"))
