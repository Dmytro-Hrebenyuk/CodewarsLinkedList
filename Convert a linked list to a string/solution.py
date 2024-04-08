def stringify(head):
    if head is None:
        return "None"
    else:
        result = ""
        probe = head
        while probe is not None:
            if probe.next is not None:
                result += str(probe.data) + ' -> '
            else:
                result += str(probe.data)
            probe = probe.next
        return result +' -> None'