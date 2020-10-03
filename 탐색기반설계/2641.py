# 숏다리의 계단 오르기 (Small) -> 재귀함수..?
n = int(input())
count=0

def stair(sum, c):
    if sum > n :
        return
    elif sum == n :
        count+=1
        return
    
    if c!=0 :
        stair(sum+1, c-1)
        stair(sum+2, c-1)
    else :
        stair(sum+1, 0)
        stair(sum+2, 0)
        stair(sum+3, 2)
stair(0,0)
print(count)
