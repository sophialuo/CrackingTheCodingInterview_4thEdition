#9.3
#Given a sorted array of n integers that has been 
#rotated an unknown number of times, give an O(logn)
#algorithm that finds an element in the array. You
#may assume that the array was originally sorted in
#increasing order
#EXMPLE
#input: find 5 in 15 16 19 20 25 1 3 4 5 7 10 14
#output: 8 (index of 5 in the array)
def search_rotated(arr, ans):
    first = 0
    end = len(arr)-1
    mid = int((first+end)/2)
    if arr == []:
        return -1
    if arr[mid] == ans:
        return mid
    
    while arr[mid] != ans:
        if arr[first] == ans:
            return first
        if arr[end] == ans:
            return end    
        #for cases like 15 16 1 3 4 5 14
        if arr[mid] < arr[first] and arr[mid] < arr[end]:
            if ans >= arr[mid] and ans <= arr[end]: #recurse right
                first = mid
            else: #recurse left
                end = mid
        #for all other cases
        else:
            if ans >= arr[first] and ans <= arr[mid]:#recurse left
                end = mid
            else: #recurse right
                first = mid 
        mid = int((first+end)/2)
    return mid
        
    
