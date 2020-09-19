# 배열 두번 출력하기

a = int(input())
b = list(map(int, input().split()))
if len(b) == a:
    for i in range(2):
        for i in b :
            print(i, end="\n")
