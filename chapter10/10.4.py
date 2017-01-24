#10.4
#Write a method to implement *, -, / operations
#You should only use the + operator
def multiply(x,  y):
    ans = 0
    for i in range(y):
        ans += x
    return ans

def subtract(x, y):
    return x + (-y)

def divide(x, y):
    count = 0
    while x != 0:
        x += -y
        count += 1
    return count

