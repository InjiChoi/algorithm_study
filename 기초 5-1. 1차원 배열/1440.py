# 비교

n = int(input())
numlist = list(map(int, input().split()))

if n == len(numlist):
    for i in range(n):
        number = numlist[i]
        if i == 0:
            number_list = numlist[1:]
        elif i == n-1:
            number_list = numlist[:-1]
        else:
            number_list = numlist[0:i]+numlist[i+1:]
        result=' '

        for j in number_list:
            if number < j:
                result += '< '
            elif number > j:
                result += '> '
            else:
                result += '= '

        print(str(i+1)+':'+result)
            