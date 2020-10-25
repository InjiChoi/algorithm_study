# 투 포인터
def two_pointer(array):
    start=0
    end=0
    total=0
    count=0

    while True:
        if total >=k:
            total -= array[start]
            start += 1
        elif end == len(array):
            break
        else:
            total += array[end]
            end += 1

        if total == k:
            count += 1

    return count

# k = 7
# a = [2, 1, 4, 3, 6, 1]
# print(two_pointer(a))