# 일곱 난쟁이

nanjang = [0 for i in range(9)]


for i in range(len(nanjang)):
    nanjang[i] = int(input())

total = sum(nanjang)
nanjang.sort()
for i in range(9):
    for j in range(i+1, 9):
        if total - nanjang[i]-nanjang[j] == 100:
            for k in range(9):
                if k==i or k==j:
                    continue
                else:
                    print(nanjang[k])
 