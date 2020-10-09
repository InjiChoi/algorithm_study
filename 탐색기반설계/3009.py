# 부분수열의 합
from itertools import combinations

n, s = map(int,input().split())
n_list = list(map(int,input().split()))
count = 0

for i in range(1,len(n_list)+1):
    answer = list(combinations(n_list, i))
    # print(answer)
    # print(" ")
    for i in range(len(answer)):
        partial_sum = sum(answer[i])
        if partial_sum == s :
            count += 1
    
print(count)