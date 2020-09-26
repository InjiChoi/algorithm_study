# 피보나치 수열 (Large)

# num = int(input())

memo={1:1,2:1}
 
def f(x) :
    if x in memo :
        return memo[x]
    memo[x]=(f(x-1)+f(x-2))%10009
    return memo[x]
 
n=int(input())
print(f(n))
 