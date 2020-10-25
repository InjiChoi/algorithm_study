# 삽입 정렬 구현
def insertion_sort(data):
    for i in range(len(data)-1):
        for j in range(i+1, 0, -1):
            if data[j-1] > data[j]:
                data[j-1], data[j] = data[j], data[j-1]
            else:
                break
    return data

# time complexity = n(n-1)/2