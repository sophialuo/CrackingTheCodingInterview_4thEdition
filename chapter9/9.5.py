#9.5
#given a sorted array of strings which is interspersed
#with empty strings, write a method to find the location
#of a given string
#example: find 'ball' in ['at', '','','', 'ball', '', '', ,'', 'car']
#return 4
#find 'ballcar' => return -1

#one way to do it
def string_loc(lst, string):
    index = 0
    while index < len(lst):
        if lst[index] == '':
            index += 1
        else:
            if lst[index] == string:
                return index

            first = lst[index][0]
            if ord(first) > ord(string[0]):
                return -1
            index += 1
        
    return -1

#another way to do it
def string_loc_binsearch(lst, string):
    first = find_nonempty_forward(lst, 0)
    end = find_nonempty_backward(lst, len(lst)-1)
    mid = find_nonempty_forward(lst, int((first+end)/2))
    if lst[first] == string:
        return first
    if lst[mid] == string:
        return mid
    if lst[end] == string:
        return end
        
    while lst[mid] != string:
        if ord(string[0]) > ord(lst[mid][0]):
            #recurse right
            first = mid
        else:
            #recurse left
            end = mid
        mid = find_nonempty_forward(lst, int((first+end)/2))
        if lst[mid] == string:
            return mid
        if first >= end:
            return -1
    return -1

def find_nonempty_forward(lst, index):
    #find next element in array that isn't ''
    if lst[index] != '':
        return index
    else:
        while lst[index] == '':
            index += 1
        return index

def find_nonempty_backward(lst, index):
    #find next element in array that isn't ''
    if lst[index] != '':
        return index
    else:
        while lst[index] == '':
            index -= 1
        return index

