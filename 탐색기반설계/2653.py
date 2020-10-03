# 규칙에 맞는 이진수 만들기 (Small)
n = int(input())
binary_list=[]
length = 2**n -1
for i in range(0, length+1):
    binary_list.append(bin(i)[2:].zfill(n))
# print(binary_list)
count = len(binary_list)

for i in binary_list:
    if '00' in i :
        count -=1
print(count)