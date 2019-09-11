import math
import random

def search_func_1(list_to_search,find_this_value):
    '''
    Search Function 1

    Aim: Scan through a list and see if the requested value is located within it.

    Input:
        - list_to_search: a list of values to search.
        - find_this_value: an integer value to located within the list.

    Return:
        The index location of the requested value in the list or -1 if
        the value is not located in the list
    '''
    def search(a,low,high,x):
        if high < low:
            return -1
        mid = math.floor(low + ((high-low)/2))
        if x == a[mid]:
            return mid
        elif x < a[mid]:
            return search(a,low,mid - 1,x)
        else:
            return search(a,mid + 1, high, x)
    return search(list_to_search,0,len(list_to_search)-1,find_this_value)


# Code to run
random.seed(1234)
my_list = [random.randint(1,10000) for i in range(1000)]
my_list.sort()
find = 9626
search_func_1(my_list,find)
