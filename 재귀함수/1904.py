# 두 수 사이의 홀수 출력하기
a, b = map(int, input().split())

def odd_print(small_n, large_n):
    if small_n > large_n :
        return
    elif large_n % 2 != 0: # 홀수일 때 출력
        odd_print(small_n, large_n-1)
        print(large_n)
    else: # 짝수이면 하나 감소시키고 넘어가기
        odd_print(small_n, large_n-1)

odd_print(a,b)
