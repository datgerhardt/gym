# Tree impl using list

def insert_left(root, child_val):
    subtree = root.pop(1)
    if len(subtree) > 1:
        root.insert(1, [child_val, subtree, []])
    else:
        root.insert(1, [child_val, [], []])
    return root

def insert_right(root, child_val):
    subtree = root.pop(2)
    if len(subtree) > 1:
        root.insert(2, [child_val, [], subtree])
    else:
        root.insert(2, [child_val, [], []])
    return root

def get_root_val(root):
    return root[0]

def set_root_val(root, new_val):
    root[0] = new_val

def get_left_child(root):
    return root[1]

def get_right_child(root):
    return root[2]

if __name__ == "__main__":
    root = [3, [], []]
    insert_left(root, 4)
    insert_left(root, 5)
    insert_right(root, 6)
    insert_right(root, 7)
    left =get_left_child(root) 
    print(left)
    
    set_root_val(left, 9)
    print(root)
    
    insert_left(left, 11)
    print(root)

    print(get_right_child(get_right_child(root)))

