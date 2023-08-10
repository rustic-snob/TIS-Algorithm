import sys
input = sys.stdin.readline

from itertools import accumulate

N, M = map(int, input().split())
table = [[0 for _ in range(N+1)]]

for i in range(N):
    table.append([prev + cur for prev, cur in zip(table[i], [0] + list(accumulate(map(int, input().split()))))])
    
for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    ans = table[x2][y2] - table[x1-1][y2] - table[x2][y1-1] + table[x1-1][y1-1]
    print(ans)
        