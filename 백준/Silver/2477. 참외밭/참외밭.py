from collections import defaultdict, deque

N = int(input())
queue = deque()
cnt = defaultdict(int)

for _ in range(6):
    temp = tuple(map(int, input().split()))
    cnt[temp[0]] += 1
    queue.append(temp)

big = set(i for i,j in cnt.items() if j == 1)

while (queue[0][0] not in big) or (queue[-1][0] not in big):
    queue.rotate(1)

print(N*(queue[0][1] * queue[-1][1] - queue[2][1] * queue[3][1]))