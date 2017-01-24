#9.7
#A circus is designing a tower routine consisting of people
#standing atop one another's shoulders. For  practical and 
#aesthetic reasons, each person must be both shorter and 
#lighter than the person below him or her. given the heights
#and weights of each person in the circus, write a method to
#compute the largest possible number of people in such a tower
#example
#input (ht, wt): (65,100)(70,150)(56,90)(75,190)(60,95)(68,110)
#output: longest tower is length 6 -- from top to bottom
#(56,90)(60,95)(65,100)(68,110)(70,150)(75,190)

def longest_tower(lst):
    max_len = 0
    sorted_lst = mergesort_pair(lst)
    for i in range(len(sorted_lst)):
        temp = longest_tower_helper(sorted_lst, i, None)
        if temp > max_len:
            max_len = temp
    return max_len

def longest_tower_helper(lst, index, prev):
    if index >= len(lst):
        return 0
    next_person = lst[index]
    if prev == None:
        return max(1+longest_tower_helper(lst, index+1, lst[index]), 
                   0+longest_tower_helper(lst, index+1, None))
    if next_person[0] > prev[0] or next_person[1] > prev[1]:
        return 0
    #take the next person or don't take the next person
    return max(1+longest_tower_helper(lst, index+1, lst[index]), 
               0+longest_tower_helper(lst, index+1, prev))
               
#sort the given list first in priority of height then weight
def mergesort_pair(lst):
    if len(lst) > 1:
        mid = int(len(lst)/2)
        left = lst[:mid]
        right = lst[mid:]
        return merge_pair(mergesort_pair(left), mergesort_pair(right))
    return lst

def merge_pair(left, right):
    left_index = 0
    right_index = 0
    ans = []
    while left_index < len(left) and right_index < len(right):
        left_elem = left[left_index]
        right_elem = right[right_index]
        if left_elem[0] > right_elem[0]:
            ans.append(left_elem)
            left_index += 1
        elif left_elem[0] < right_elem[0]:
            ans.append(right_elem)
            right_index += 1
        else:
            if left_elem[1] > right_elem[1]:
                ans.append(left_elem)
                left_index += 1
            else:
                ans.append(right_elem)
                right_index += 1
    if left_index < len(left):
        ans.extend(left[left_index:])
    if right_index < len(right):
        ans.extend(right[right_index:])
    return ans




#test cases
 
test_lst = [(65,100),(70,150),(56,90),(65,91),(75,190),(60,95),(68,110)]
sorted_lst = mergesort_pair(test_lst)
print(sorted_lst)
print(longest_tower(sorted_lst))

test_lst = [(12, 12), (11,  8), (10,  9), ( 9, 10), ( 8, 11), ( 7,  7)]
sorted_lst = mergesort_pair(test_lst)
print(sorted_lst)
print(longest_tower(sorted_lst))
