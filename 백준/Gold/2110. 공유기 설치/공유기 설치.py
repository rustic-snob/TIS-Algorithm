import sys

input = sys.stdin.readline

N, C = map(int, input().split())
houses = []
for _ in range(N):
    houses.append(int(input()))

houses.sort()

l = 1
r = houses[-1]-houses[0]

while l <= r:
    m = (l+r)//2
    cur_houses = houses[:]
    iptime = 1
    dist = 0
    for h1, h2 in zip(cur_houses[:-1], cur_houses[1:]):
        dist += h2-h1
        if dist < m:
            pass
        else:
            iptime+=1
            dist=0
    if iptime >= C:
        ans = m
        l = m+1
    else:
        r = m-1
        

print(ans)