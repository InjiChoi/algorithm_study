# C언어를 찾아라

a = input().upper()
num_c = 0
num_cc = 0

for i in range(len(a)):
    if a[i] == 'C':
        num_c += 1
        if i !=len(a)-1 and a[i+1] =='C' :
            num_cc += 1
print(num_c)
print(num_cc)