#8.1 
#Write a method to generate nth Fibonacci number
def fib_recursion(n):
    if n <= 1:
        return 1
    return fib_recursion(n-1) + fib_recursion(n-2)

#a more space and time efficient way    
def fib_efficient(n):
    first = 0
    second = 1
    for i in range(n):
        temp = second
        second += first
        first = temp
    return second

