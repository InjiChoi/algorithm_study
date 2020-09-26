# 우박수(3n+1) (reverse)
num = int(input())

def woobaksoo(n):
    if n == 1:
        return
    elif n % 2 == 0:
        n = n / 2
        woobaksoo(n)
        print(int(n))
    elif n % 2 != 0:
        n = 3*n + 1
        woobaksoo(n)
        print(int(n))
        
woobaksoo(num)
print(num)