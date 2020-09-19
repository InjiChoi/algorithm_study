# 거꾸로 출력하기 3

a = int (input())
b = list(map(int, input().split())) # a개 넘어도 입력되는데 괜찮은건지
b.reverse()
if len(b) == a:
    for i in b:
        print(i, end=' ')