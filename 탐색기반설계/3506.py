# 블럭 채우기 1 (Small)
num = int(input())

def block(n):
    if n==1:
        return 1
    elif n==2:
        return 2
    else:
        return block(n-1)+block(n-2)

print(block(num))