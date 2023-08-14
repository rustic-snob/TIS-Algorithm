from math import gcd

n1, d1 = map(int, input().split())
n2, d2 = map(int, input().split())

g = gcd((n3:=d2*n1+d1*n2), d3:=d1*d2)
print(n3//g, d3//g)