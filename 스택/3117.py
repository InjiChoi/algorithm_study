# 0은 빼!
n = int(input())
i_list = list()
swp = 0 

for i in range(n):
    a = int(input())
    if a == 0:
        i_list.pop()
    else:
        i_list.append(a)

for i in i_list:
    swp += i
print(swp)