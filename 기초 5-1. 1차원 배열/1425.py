# 자리 배치

num, line_max = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
if num == len(nums):
    for i in range(0,int(num/line_max)+1):
        for j in range(i*line_max, (i+1)*line_max):
            if j >= len(nums):
                break
            print(nums[j], end=' ')
        print()
    