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
    my_list["elements"] = element
    my_list["size"] += 1
    
def add_last(my_list, element):
    my_list["elements"].append(element)
    my_list["size"] += 1

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
    return my_list["elements"].pop(0)

def remove_last(my_list):
    return my_list["elements"].pop()

def insert_element(my_list, element, pos):
    my_list["elements"].insert(pos,element)