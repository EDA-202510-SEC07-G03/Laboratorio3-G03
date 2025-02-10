from DataStructures.List import list_node as ln

def new_list():
    newlist={"first":None,
             "last":None,
             "size":0}
    return(newlist)

def get_element (my_list,pos):
    searchpos=0
    node=my_list["first"]
    while searchpos < pos:
        node=node["next"]
        searchpos +=1
    return node["info"]

def is_present(my_list, element, cmp_function):
    is_in_array = False
    temp= my_list["first"]
    count=0
    while not is_in_array and temp is not None:
        if cmp_function(element,temp["info"]) == 0:
            is_in_array = True
        else:
            temp =temp["next"]
            count+=1
    if not is_in_array:
        count=-1
    return (count)


def add_first(my_list,element):
    """
    Añade un elemento al principio de la estructura de datos: single linked list.
    """
    new_node=ln.new_single_node(element)
    new_node["next"]=my_list["first"]
    my_list["first"]=new_node
    
    if my_list["size"] == 0:
        my_list["last"]=new_node
        
    my_list["size"]+=1
    return(my_list)

def add_last(my_list,element):
    """
    Añade un elemento al final de la estructura de datos
    """
    new_node=ln.new_single_node(element)
    my_list["last"]=new_node
    
    if my_list["size"]==0:
        my_list["first"]=new_node
    
    my_list["size"]+=0
    
    return my_list
def size(my_list):
    return my_list["size"]

def first_element(my_list):
    if size(my_list) == 0:
        raise Exception('IndexError: list index out of range')
    return my_list["first"]