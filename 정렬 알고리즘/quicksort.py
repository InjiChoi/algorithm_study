# 퀵 정렬 구현
def quicksort(data):
    if len(data)<1:
        return data
    
    left = list()
    right = list()
    pivot = data[0]

    for i in range(1, len(data)):
        if pivot > data[i]:
            left.append(data[i])
        else:
            right.append(data[i])

    return quicksort(left) + [pivot] + quicksort(right)

# time complexity = n*logn

# test
# a = [26, 27, 42, 10, 14, 19, 35, 20]
# print(quicksort(a))