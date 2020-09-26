num = int(input())

def recursion_func(n):
    if n==0:
        return
    print(n)
    recursion_func(n-1)

recursion_func(num)