# 삼각화단 만들기 (Small)
n = int(input())
count = 0
for a in range(1, n):
    for b in range(1, n):
        for c in range(1, n):
            if (a<=b and b<=c and a+b>c and a+b+c==n):
                count +=1

print(count)