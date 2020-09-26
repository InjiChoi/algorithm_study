# 우박수(3n+1) (basic)
num = int(input())

def woobaksoo(n):
    if n == 1:
        return
    elif n % 2 == 0:
        n = n / 2
        print(int(n))
        woobaksoo(n)
    elif n % 2 != 0:
        n = 3*n + 1
        print(int(n))
        woobaksoo(n)
print(num)
woobaksoo(num)