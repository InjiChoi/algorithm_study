# 숫자 로테이션

# collections 모듈 deque(데크) : rotate 메소드 활용
from collections import deque

n = int(input())
nums = deque(list(map(int,input().split())))

if len(nums) == n:
    for i in range(n):
        for a in nums:
            print(a, end=" ")
        nums.rotate(-1)
        print()