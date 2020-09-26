# 1부터 n까지 출력하기
num = int(input())

def recursion_print(n):
    if n!=1:
        recursion_print(n-1)
    print(n)

recursion_print(num)