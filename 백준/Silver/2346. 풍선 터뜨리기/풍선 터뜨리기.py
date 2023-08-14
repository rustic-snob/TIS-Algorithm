from collections import deque

N = int(input())
balloons = deque((idx+1, com) for idx, com in enumerate(map(int, input().split())))
ans = []
while balloons:
     balloon, com = balloons.popleft()
     ans.append(balloon)
     if com > 0:
         balloons.rotate(-com+1)
     else:
         balloons.rotate(-com)
print(' '.join(map(str, ans)))