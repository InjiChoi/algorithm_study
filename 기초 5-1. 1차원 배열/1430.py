# 기억력 테스트 2

n = int(input())
num_list = list(map(int, input().split()))

m = int(input())
quiz = list(map(int, input().split()))

if n==len(num_list) and m==len(quiz):
    for i in quiz:
        for j in num_list:
            if i == j:
                result=1
                break
            result=0      
        print(result, end=' ')
