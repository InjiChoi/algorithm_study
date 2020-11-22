# 소들의 헤어스타일
class Stack: 
    def __init__(self):
        self.len  = 0
        self.list = []

    def push(self, num):
        self.list.append(num)
        self.len += 1

    def pop(self):
        if self.size() == 0:
            return -1
        pop_result = self.list[self.len-1]
        del self.list[self.len - 1]
        self.len -= 1

        return pop_result

    def size(self):
        return self.len
    
    def empty(self):
        return 1 if self.len == 0 else 0

    def top(self):
        return self.list[-1] if self.size() != 0 else -1


n     = int(input()) # 소들의 개수 입력
stack = Stack()      # stack 선언
cnt   = 0            # 볼 수 있는 소의 케이스 결과의 개수


for _ in range(n) : #{
    #print(stack.list, c)
    c = int(input()) # 소의 키를 입력으로 받음

    if stack.empty() : # stack이 비어있다면 c를 push 해줌
        stack.push(c)

    elif stack.top() <= c : # 만약 stack의 top이 c보다 작다면 c를 보지 못하므로 pop으로 삭제해줌
        stack.pop()
        while stack.top() <= c and stack.top() != -1 : # 마찬가지로 stack의 top이 c를 볼 수 있을 때까지 pop으로 삭제해줌
            stack.pop()
        stack.push(c)   # stack에 c 소의 스타일을 볼 수 있는 소들만 남아있으므로 push 해줌     
  
    else : stack.push(c) # stack에 c 소의 스타일을 볼 수 있는 소들만 남아있으므로 push 해줌   

    cnt += stack.size() - 1 # c를 볼 수 있는 소들의 수를 cnt에 더해준다.
#}

print(cnt)