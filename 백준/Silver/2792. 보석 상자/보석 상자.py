import math
import sys

input = sys.stdin.readline

N, M = map(int, input().split())

gems = []

for _ in range(M):
    gems.append(int(input()))
    
l = 1
r = max(gems)

while l<=r:
    m = (l+r)//2
    if sum([math.ceil(gem/m) for gem in gems]) <= N:
        ans = m
        r = m-1
    else:
        l = m+1
print(ans)

