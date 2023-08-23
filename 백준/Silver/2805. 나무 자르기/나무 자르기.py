N, M = map(int, input().split())
trees = list(map(int, input().split()))

l = 0
r = max(trees)-1

ans = 0

while l <= r:
    m = (l+r)//2
    if sum([cur if (cur:=tree - m)>0 else 0 for tree in trees]) >= M:
        ans = m
        l = m+1
    else:
        r = m-1

print(ans)