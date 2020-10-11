# 서울에서 경산까지 (tiny)
n, k = map(int,input().split())
# walktime, w_money, bicycletime, b_money
lst=[0 for i in range(n)]
for i in range(n):
    lst[i] = list(map(int, input().split()))

def solution(K, travel):
    answer = 0
