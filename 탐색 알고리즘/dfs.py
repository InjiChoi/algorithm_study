# 깊이 우선 탐색(DFS): stack

# 방법1. Stack 활용
def dfs(graph, start):
    visited = []
    stack = []
    stack.append(start)

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            stack.extend(graph[node])
    return visited

# 방법2. 재귀함수 이용
def r_dfs(graph, start, visited):
    visited.append(start)
    for node in graph[start]:
        if node not in visited:
            r_dfs(graph, node, visited)
    return visited

# For test
graph = {'A':['B','C'],
         'B':['A','D','E'],
         'C':['A','F','G'],
         'D':['B'],
         'E':['B'],
         'F':['C','H'],
         'G':['C'],
         'H':['E','F']}

print(dfs(graph, 'A'))
print(r_dfs(graph, 'A', []))