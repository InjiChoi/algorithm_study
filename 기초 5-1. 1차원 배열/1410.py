# 올바른 괄호 1 (괄호 개수 세기)

a = input()
openb = 0
closeb = 0

for i in range(len(a)):
    if a[i] == "(":
        openb+=1
    elif a[i] == ")":
        closeb+=1

print(openb, closeb)