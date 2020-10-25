# 선택 정렬 구현
def selectionsort(data):
    for i in range(len(data)-1):
        lowest = i
        
        for j in range(i+1, len(data)):
            if data[lowest] > data[j]:
                lowest = j

        data[lowest], data[i] = data[i], data[lowest]
    
    return data

# time complexity = n(n-1)/2