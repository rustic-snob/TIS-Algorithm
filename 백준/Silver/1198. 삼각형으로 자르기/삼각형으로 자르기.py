from itertools import combinations

XY = [tuple(map(int, input().split())) for _ in range(int(input()))]

ans = -float('inf')

for xy in combinations(XY, 3):
    temp = xy[0][0] * xy[1][1] + xy[1][0] * xy[2][1] + xy[2][0] * xy[0][1] - \
           xy[1][0] * xy[0][1] - xy[2][0] * xy[1][1] - xy[0][0] * xy[2][1]
    if abs(temp) > ans:
        ans = abs(temp)
    
print(ans/2)