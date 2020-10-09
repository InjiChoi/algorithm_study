# 일곱 난쟁이

nanjang = [0 for i in range(9)]

for i in range(len(nanjang)):
    nanjang[i] = int(input())

nanjang.sort()

for i in nanjang:
    print(i)
