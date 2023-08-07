import sys
input = sys.stdin.readline

from collections import deque

V, E = int(input()), int(input())
networks = [[] for _ in range(V)]
visited = set([0])
ans = 0

for _ in (range(E)):
    v1, v2 = map(lambda x: int(x)-1, input().split())
    networks[v1].append(v2)
    networks[v2].append(v1)

queue = deque(networks[0])

while queue:
    cur = queue.popleft()
    if cur not in visited:
        visited.add(cur)
        ans += 1
        queue.extend(networks[cur])
        
print(ans)