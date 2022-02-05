import Queuee.linked_queue as q
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
tea = Tree_node("tea")
coffee = Tree_node("coffee")
left_child.left_child = tea
left_child.right_child = coffee
non_al = Tree_node("non_alcoholic")
al = Tree_node("alcoholic")
right_child.left_child = non_al
right_child.right_child = al
green = Tree_node("green")
black = Tree_node("black")
tea.left_child = green
tea.right_child = black
mild = Tree_node("mild")
green.left_child = mild

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


#in_order_traversal(new_bt)

def post_order_traversal(root_node):
    if not root_node:
        return
    post_order_traversal(root_node.left_child)
    post_order_traversal(root_node.right_child)
    print(root_node.data)

#post_order_traversal(new_bt)

def level_order_traversal(root_node):
    if not root_node:
        return
    else:
        custom_queue = q.Queue()
        custom_queue.enqueue(root_node)
        while not(custom_queue.isEmpty()):
            root = custom_queue.dequeue()
            print(root.value.data)
            if root.value.left_child is not None:
                custom_queue.enqueue(root.value.left_child)
            if root.value.right_child is not None:
                custom_queue.enqueue(root.value.right_child)
        
#level_order_traversal(new_bt)
def search_bt(root_node, node_value):
    if not root_node:
        return "The BT does not exist"
    else:
        custom_queue = q.Queue()
        custom_queue.enqueue(root_node)
        while not (custom_queue.isEmpty()):
            root = custom_queue.dequeue()
            if root.value.data == node_value:
                print(root.value.data)
                return "This node exist"
            if root.value.left_child is not None:
                custom_queue.enqueue(root.value.left_child)
            if root.value.right_child is not None:
                custom_queue.enqueue(root.value.right_child)
        return "The node does not exist"

#print(search_bt(new_bt,"mild"))

def insert_bt(root_node, new_node):
    if not root_node:
        root_node = new_node
    else:
        custom_queue = q.Queue()
        custom_queue.enqueue(root_node)
        while not(custom_queue.isEmpty()):
            root = custom_queue.dequeue()
            if root.value.left_child is not None:
                custom_queue.enqueue(root.value.left_child)
            else:
                root.value.left_child = new_node
                return "Node inserted"
            if root.value.right_child is not None:
                custom_queue.enqueue(root.value.right_child)
            else:
                root.value.right_child = new_node
                return "Node inserted"

# new_node = Tree_node("americano")
# insert_bt(new_bt, new_node)
# level_order_traversal(new_bt)

def  get_deepest_node(root_node):
    if not root_node:
        return
    else:
        custom_queue = q.Queue()
        custom_queue.enqueue(root_node)
        while not(custom_queue.isEmpty()):
            root = custom_queue.dequeue()
            if root.value.left_child is not None:
                custom_queue.enqueue(root.value.left_child)
            if root.value.right_child is not None:
                custom_queue.enqueue(root.value.right_child)
        deepest_node = root.value
        return deepest_node

#print(get_deepest_node(new_bt).data)

def delete_deepest_node(root_node, d_node):
    if not root_node:
        return
    else:
        custom_queue = q.Queue()
        custom_queue.enqueue(root_node)
        while not(custom_queue.isEmpty()):
            root = custom_queue.dequeue()
            if root.value is d_node:
                root.value = None
                return
            if root.value.right_child:
                if root.value.right_child is d_node:
                    root.value.right_child = None
                    return
                else:
                    custom_queue.enqueue(root.value.right_child)
            if root.value.left_child:
                if root.value.left_child is d_node:
                    root.value.left_child = None
                    return
                else:
                    custom_queue.enqueue(root.value.left_child)

# deepest_node = get_deepest_node(new_bt)
# delete_deepest_node(new_bt, deepest_node)
# deepest_node = get_deepest_node(new_bt)
# delete_deepest_node(new_bt, deepest_node)
# level_order_traversal(new_bt)


def delete_node_bt(root_node, node):
    if not root_node:
        return "The BT does not exist"
    else:
        custom_queue = q.Queue()
        custom_queue.enqueue(root_node)
        while not(custom_queue.isEmpty()):
            root = custom_queue.dequeue()
            if root.value.data == node:
                d_node = get_deepest_node(root_node)
                root.value.data = d_node.data
                delete_deepest_node(root_node, d_node)
                return 'The node has been deleted'
            if root.value.left_child is not None:
                custom_queue.enqueue(root.value.left_child)
            if root.value.right_child is not None:
                custom_queue.enqueue(root.value.right_child)
        return "Failed"

# delete_node_bt(new_bt, 'tea')
# level_order_traversal(new_bt)
def delete_bt(root_node):
    root_node.data = None
    root_node.left_child = None
    root_node.right_child = None
    return "The bt has been deleted"

# delete_bt(new_bt)
# level_order_traversal(new_bt)
