# 병합 정렬 구현
def merge_sort(left, right):
	merged = list()

	left_index = 0
	right_index = 0

	while left_index < len(left) and right_index < len(right):
		if left[left_index] < right[right_index]:
			merged.append(left[left_index])
			left_index += 1
		else:
			merged.append(right[right_index])
			right_index += 1

	while left_index < len(left):
		merged.append(left_index)
		left_index += 1

	while right_index < len(right):
		merged.append(right_index)
		right_index += 1

	return merged

def split(data):
    if len(data)<=1:
        return data
    
    mid = len(data)//2

    left = split(data[:mid])
    right = split(data[mid:])

    return merge_sort(left, right)


a = [26, 27, 42, 10, 14, 19, 35, 20]
print(split(a))