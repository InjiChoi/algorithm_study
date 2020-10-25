# 이분 탐색
def binary_search(array, target):
    lower = 0
    upper = len(array)

    while lower <= upper:
        mid = (lower+upper)//2

        if array[mid] == target:
            return True
        elif array[mid] < target:
            lower = mid+1
        elif array[mid] > target:
            upper = mid-1

    return False

# time complexity = logn