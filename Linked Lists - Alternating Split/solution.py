class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None
    
class Context(object):
    def __init__(self, first, second):
        self.first = first
        self.second = second
    
def alternating_split(head):
    if head is None or head.next is None:
        raise ValueError("List must have at least two nodes")

    first_head = None
    second_head = None
    first_tail = None
    second_tail = None

    current = head
    i = 1
    while current:
        if i % 2 == 1:
            if first_head is None:
                first_head = current
                first_tail = current
            else:
                first_tail.next = current
                first_tail = current
        else:
            if second_head is None:
                second_head = current
                second_tail = current
            else:
                second_tail.next = current
                second_tail = current

        current = current.next
        i += 1
    if first_tail:
        first_tail.next = None
    if second_tail:
        second_tail.next = None
    return Context(first_head, second_head)