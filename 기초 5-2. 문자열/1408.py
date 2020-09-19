# 암호 처리

a = input()

for i in a:
    i = ord(i) + 2
    i = chr(i)
    print(i, end='')
print()
for j in a:
    j = (ord(j) * 7) % 80 + 48
    j = chr(j)
    print(j, end='')