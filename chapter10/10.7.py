#10.7
#Design an algorithm to find the kth number such 
#that the only prime factors are 3, 5, and 7


def kth_number(k):
    if k == 1:
        return 1
    q3 = [3,]
    q5 = [5,]
    q7 = [7,]
    for i in range(k-2):
        min3 = q3[0]
        min5 = q5[0]
        min7 = q7[0]
        if min3 == min5 or min3 == min7:
            q3.pop(0)
            min3 = q3[0]
        if min5 == min7:
            q5.pop(0)
            min5 = q5[0]
            
        if min3 < min5 and min3 < min7:
            q3.pop(0)
            q3.append(min3*3)
            q5.append(min3*5)
            q7.append(min3*7)
        elif min5 < min3 and min5 < min7:
            q5.pop(0)
            q3.append(min5*3)
            q5.append(min5*5)
            q7.append(min5*7)
        else:
            q7.pop(0)
            q3.append(min7*3)
            q5.append(min7*5)
            q7.append(min7*7)
    return min(q3[0], min(q5[0], q7[0]))
        