def new_list():
    newlist = {
        "elements": [],
        "size": 0,
    }
    return newlist

def get_element(my_list, index):
    
    return my_list["elements"][index]


def is_present(my_list, element, cmp_function):
    
    size = my_list["size"]
    if size > 0:
        keyexist = False
        for keypos in range(0,size):
            info = my_list["elements"][keypos]
            if cmp_function(element, info) == 0:
                keyexist = True
                break
        if keyexist:
            return keypos
    return -1

def add_first(my_list, element):
    my_list["elements"].insert(0, element)
    my_list["size"] += 1
    return my_list
    
def add_last(my_list, element):
    my_list["elements"].append(element)
    my_list["size"] += 1
    return my_list

def size(my_list):
    return my_list["size"]

def is_empty(my_list):
    if my_list["size"] == 0:
        result = True
    else:
        result = False
    return result

def first_element(my_list):
    return my_list["elements"][0]

def last_element(my_list):
    return my_list["elements"][-1]

def remove_first(my_list):
    my_list["elements"].pop(0)
    my_list["size"] -= 1
    return my_list

def remove_last(my_list):
    my_list["elements"].pop()
    my_list["size"] += 1
    return my_list

def insert_element(my_list, element, pos):
    my_list["elements"].insert(pos,element)
    my_list["size"] += 1
    return my_list

def delete_element(my_list, element):
    my_list["elements"].pop(element)
    my_list["size"] -= 1
    return my_list

def change_info(my_list, pos, new_info):
    my_list["elements"][pos] = new_info
    return my_list

def exchange(my_list, pos_1, pos_2):
    pos1 = my_list["elements"][pos_1]
    pos2 = my_list["elements"][pos_2]
    my_list["elements"][pos_1] = pos2
    my_list["elements"][pos_2] = pos1
    return my_list
    
def sub_list(my_list, pos_i, num_elements):
    sub_list = new_list()
    sub_list["size"] = num_elements
    for i in range(pos_i, pos_i+num_elements):
        sub_list["elements"].append(my_list["elements"][i])
    return sub_list