n = int(input()) #숫자 갯수
n_list = list(map(int, input().split()[:n]))

m = int(input()) #질문의 수
m_list = list(map(int, input().split()[:m]))

# 이진탐색함수
def binarySerch(lst, key):
    low=0
    high=len(lst)-1

    while high >= low:
        mid = (high+low)//2

        if key < lst[mid]:
            high = mid-1
        elif key == lst[mid]:
            return mid+1
        else:
            low=mid+1
    return -1

for i in m_list:
    print(binarySerch(n_list, i), end=' ')


# 시간초과
# for i in m_list:
#     if i in n_list:
#         print(n_list.index(i)+1, end=' ')
#     else:
#         print(-1, end=' ')