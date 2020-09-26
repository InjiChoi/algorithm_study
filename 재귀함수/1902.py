# 1부터 n까지 역순으로 출력하기
num = int(input())

def recursion_func(n):
    if n==0:
        return
    print(n)
    recursion_func(n-1)

recursion_func(num)