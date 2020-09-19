# 빠진 카드

a = int(input())
card = list(range(1, a+1))

for i in range(len(card)-1):
    num = int(input())
    card.remove(num)
print(card[0])        