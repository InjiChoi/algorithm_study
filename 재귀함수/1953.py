# 삼각형 출력하기 1
num = int(input())
def triangle_print(n):
    if n==1:
        print('*')
        return
    triangle_print(n-1)
    print('*'*n)

triangle_print(num)
