import random
def search_func_2(list_to_search,find_this_value):
    '''
    Search Function 2

    Aim: Scan through a list and see if the requested value is located within it.

    Input:
        - list_to_search: a list of values to search.
        - find_this_value: an integer value to located within the list.

    Return:
        The index location of the requested value in the list or -1 if
        the value is not located in the list
    '''
    for i in range(len(list_to_search)):
        if list_to_search[i] == find_this_value:
            return i
    return -1

# Code to Run
random.seed(1234)
my_list = [random.randint(1,10000) for i in range(1000)]
my_list.sort()
find = 9626
search_func_2(my_list,find)
