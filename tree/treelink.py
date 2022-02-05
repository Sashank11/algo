class Tree_node:
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None
    




new_bt = Tree_node("Drinks")
left_child = Tree_node("Hot")
right_child = Tree_node("cold")
new_bt.left_child = left_child
new_bt.right_child = right_child


def pre_order_traversal(root_node):
    if not root_node:
        return
    print(root_node.data)
    pre_order_traversal(root_node.left_child)
    pre_order_traversal(root_node.right_child)

#pre_order_traversal(new_bt)

def in_order_traversal(root_node):
    if not root_node:
        return
    in_order_traversal(root_node.left_child)
    print(root_node.data)
    in_order_traversal(root_node.right_child)


in_order_traversal(new_bt)