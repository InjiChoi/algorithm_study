# 숫자 거꾸로 출력하기
from sys import stdin

n_list = list(input())

for i in range(len(n_list)):
    print(n_list.pop(), end="")