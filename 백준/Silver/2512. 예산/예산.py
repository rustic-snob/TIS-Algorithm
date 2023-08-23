_ = input()
provinces = list(map(int, input().split()))
maginot = int(input())

l = 1
r = max(provinces)
ans = 1

while l<=r:
    m = (l+r)//2
    if sum([min(m,province) for province in provinces]) <= maginot:
        ans = m
        l = m+1
    else:
        r = m-1
print(ans)