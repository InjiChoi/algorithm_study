# (python)삼각화단 만들기 (Large)
# # 삼각화단 만들기 (Small)
n = int(input())
count=0

for k in range(n//3, n//2 + 1) :
    for i in range(1, n//3 + 1) :
        j = n - (i+k)
        if i <= j and j <= k and i+j > k :
            count += 1

print(count)