# 알파벳 개수 출력하기

a = input()
alphabet=['a','b','c','d','e','f','g','h',
        'i','j','k','l','m','n','o','p',
        'q','r','s','t','u','v','w','x','y','z']
for i in alphabet:
    print(str(i)+':'+str(a.count(i)))