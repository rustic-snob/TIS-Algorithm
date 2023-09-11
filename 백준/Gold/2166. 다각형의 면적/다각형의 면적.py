xy = [tuple(map(int, input().split())) for _ in range(int(input()))]

ans = 0

for i in range(1, len(xy)-1):
    temp = xy[0][0] * xy[i][1] + xy[i][0] * xy[i+1][1] + xy[i+1][0] * xy[0][1] - \
           xy[i][0] * xy[0][1] - xy[i+1][0] * xy[i][1] - xy[0][0] * xy[i+1][1]
    ans += temp / 2
    
print(round(abs(ans), 1))

