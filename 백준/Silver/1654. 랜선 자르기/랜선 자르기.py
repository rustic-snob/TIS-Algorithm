import sys
input = sys.stdin.readline

K, N = map(int, input().split())
l = 1
r = 0
lan = []

for _ in range(K):
    tmp = int(input())
    if tmp > r:
        r = tmp
    lan.append(tmp)

if r==l:
    print(1)
    sys.exit(0)

mid = (r-l) // 2
 
def can_make(lan, i, N):
    tot = 0
    for l in lan:
        tot += l // i
    if tot < N:
        return False
    else:
        return True

while l <= r:
    if can_make(lan, mid, N):
        ans = mid
        l = mid+1
        mid = (r+l) // 2
    else:
        r = mid-1
        mid = (r+l) // 2
        
print(ans)