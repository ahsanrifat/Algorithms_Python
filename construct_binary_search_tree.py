class Node:
    def __init__(self, value, parent, left_child, right_child):
        self.value: int = value
        self.parent: Node = parent
        self.left_child: Node = left_child
        self.right_child: Node = right_child

    def __str__(self):
        parent = self.parent != None and self.parent.value or None
        left_child = self.left_child != None and self.left_child.value or None
        right_child = self.right_child != None and self.right_child.value or None
        return f"Self->{self.value}, Left->{left_child}, Right->{right_child}"


def make_root(root_value):
    return Node(root_value, None, None, None)


def insert_child(root_node: Node, child_value):
    left_node: Node = root_node.left_child
    right_node: Node = root_node.right_child
    if child_value < root_node.value:
        if left_node == None:
            print("Left None")
            root_node.left_child = Node(child_value, root_node, None, None)
            print(root_node)
            return
        else:
            insert_child(root_node.left_child, child_value)
            return
    elif child_value >= root_node.value:
        if right_node == None:
            print("Right None")
            root_node.right_child = Node(child_value, root_node, None, None)
            print(root_node)
            return
        else:
            insert_child(root_node.right_child, child_value)
            return


def traverse_bst(root_node: Node):
    if root_node == None:
        return
    left_node: Node = root_node.left_child
    right_node: Node = root_node.right_child
    if left_node != None:
        print(f"Left Child {left_node.value}")
    traverse_bst(left_node)
    if right_node != None:
        print(f"Right Child {right_node.value}")
    traverse_bst(left_node)


input_list = [6, 12, 4, 5, 32, 33, 3, 6, 15, 20]

make_root_flag = False
root_node = None
for value in input_list:
    if make_root_flag == False:
        root_node = make_root(value)
        make_root_flag = True
    else:
        if root_node != None:
            print(f"Inserting-----{value}-------")
            insert_child(root_node, value)
# traverse_bst(root_node)