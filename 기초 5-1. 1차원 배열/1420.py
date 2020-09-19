# 3등 찾기

num=int(input())
scores=[]
for i in range(num):
    name,score=input().split()
    scores.append((name,int(score)))

scores.sort(key=lambda score:score[1],reverse=True)
print(scores[2][0])

