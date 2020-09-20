# 2진수 변환

num = int(input())
r_list = []
if num==0: print(0)
while(num!=0):
    quotient = num//2
    remainder = num%2
    num = quotient
    r_list.append(remainder)
r_list.reverse()
for a in r_list:
    print(a, end='')

# print(str(bin(int(input())))[2:])