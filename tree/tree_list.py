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
            if self.custom_list[i +1] == node_value:
                return "Node found " + "N" + str(i +1)
        return "Node not found"

    def pre_order_traversal(self, index):
        if index > self.last_used_index:
            return
        print(self.custom_list[index])
        self.pre_order_traversal(index*2)
        self.pre_order_traversal(index*2 +1)

    def in_order_traversal(self,index):
        if index > self.last_used_index:
            return
        self.in_order_traversal(index*2)
        print(self.custom_list[index])
        self.pre_order_traversal(index*2 +1)


    def post_order_traversal(self, index):
        if index > self.last_used_index:
            return
        self.post_order_traversal(index*2)
        self.post_order_traversal(index*2 +1)
        print(self.custom_list[index])

    def level_order_traversal(self, index):
        # if index > self.last_used_index:
        #     return
        # print(self.custom_list[index])
        # self.level_order_traversal(index+1)
        # This is bad as it takes space
        for i in range(index, self.last_used_index + 1):
            print(self.custom_list[i])
        
    def delete_node(self, node_value):
        if self.last_used_index == 0:
            return "There is no node to delete"
        for i in range(1, self.last_used_index+1):
            if self.custom_list[i] == node_value:
                self.custom_list[i] = self.custom_list[self.last_used_index]
                self.custom_list[self.last_used_index] = None
                self.last_used_index -=1
                return "The node has been deleted"

    def delete_bt(self):
        self.custom_list = None
        return "The bt has been successfully deleted"


new_bt = Binary_tree(8)
new_bt.insert_node("Drinks")
new_bt.insert_node("Hot")
new_bt.insert_node("Cold")
new_bt.insert_node("Tea")
new_bt.insert_node("Coffee")
#print(new_bt.search_node("Cold"))
#new_bt.pre_order_traversal(1)
#new_bt.in_order_traversal(1)
#new_bt.post_order_traversal(1)
print(new_bt.delete_node("Hot"))
#print(new_bt.delete_bt())
new_bt.level_order_traversal(1)