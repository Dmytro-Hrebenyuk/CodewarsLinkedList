from preloaded import Node

'''
Node is defined in preloaded like this:

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''
    
def push(head, data):
    new_node = Node(data)
    new_node.next = head
    return new_node

def build_one_two_three():
    none = None
    node1 = push(none, 3)
    node2 = push(node1, 2)
    node3 = push(node2, 1)
    return node3