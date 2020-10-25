# 버블 정렬 구현
def bubble_sort(data):
    for i in range(len(data-1)):
        for j in range(len(data-1-i)):
            if data[j]<data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
    return data

# time complexity = n(n-1)/2