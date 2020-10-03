# 케익 자르기
a, b = map(int, input().split())
c, d = map(int, input().split())

if a > b : # a, b 대소 순서 정렬
    a, b = b, a

check = 0 # cross 인지 check할 변수

for i in c, d: # c와 d 둘 중 하나만 사이에 껴있으면 1
    if a < i < b:
        check += 1

if check == 1:
    print("cross")
else:
    print("not cross")