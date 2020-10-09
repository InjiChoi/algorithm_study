# 숏다리의 계단 오르기 (Small) -> DFS
def dfs(total, three):
    global n, count
    if total == n: # n과 같으면 count+1
        count +=1
        return
    elif total > n: # n보다 크면 나가리 더이상 탐색x
        return
    else:
        # 만약 3칸을 올라갔다면 1칸, 2칸을 밟으면서 기회 1번씩 사용
        dfs(total+1, three-1)
        dfs(total+2, three-1)
        if three <= 0: # 0보다 작거나 같다면 3칸을 가지 않았으므로 3칸 갈 수 있음
            dfs(total+3, 2) # 3칸 올라가면서 2번의 기회

n = int(input())
count = 0

dfs(0, 0)

print(count)