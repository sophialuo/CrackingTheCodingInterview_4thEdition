#8.3
#write a method that returns all subsets of a set
    
#note: array parameter is an array of strings
def subsets(array):
    all = []
    for i in range(len(array)):
        all.append(subsets_helper(array[i], array[i+1:]))
    return all
        
def subsets_helper(elem, array):
    if array == []:
        return [elem]
    return subsets_helper(elem, array[1:]) + subsets_helper(elem + array[0], array[1:])
    
