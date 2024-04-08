def linked_list_from_string(s):
    if s == None:
        return None
    
    related_list = None
    
    list_values = s.split(' -> ')
    
    for i in range(1, len(list_values)):
        if related_list == None:
            related_list = Node(int(list_values[-i-1]))
        else:
            related_list = Node(int(list_values[-i-1]), related_list) 
            
    return related_list