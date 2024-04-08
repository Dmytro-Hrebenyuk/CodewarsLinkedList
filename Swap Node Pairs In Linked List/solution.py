from preloaded import Node

def swap_pairs(head):
    if not head or not head.next:
        return head
    prev = None
    current = head
    while current and current.next:
        next_node = current.next
        current.next = next_node.next
        next_node.next = current
        if prev:
            prev.next = next_node
        else:
            head = next_node
        prev = current
        current = current.next
    return head