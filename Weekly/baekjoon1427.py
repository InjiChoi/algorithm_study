# 소트인사이드
s = input()
    # new_s=[]
    # for i in range(len(s)):
    #     num = int(s[i])
    #     new_s.append(num)
new_s = [int(n) for n in s]
new_s.sort()
new_s.reverse()

for i in new_s:
    print(i, end='')