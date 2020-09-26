# # 1부터 n까지 합 구하기
# import sys
# sys.setrecursionlimit(10000) # recursive depth increase
# # ==> stack overflow ㅠㅠ
# num = int(input())

# def sum_num(n):
#     if n <= 1:
#         return 1
#     return n + sum_num(n-1)

# print(sum_num(num))

