# 디지털 도어 락
from math import gcd
a, b, c = map(int, input().split())
gcd1 = gcd(a,b)
gcd2 = gcd(b,c)

print(gcd(gcd1, gcd2))
