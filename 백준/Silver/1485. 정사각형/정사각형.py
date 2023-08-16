import sys
from itertools import combinations
input = sys.stdin.readline

for _ in range(int(input())):
    coords = [tuple(map(int, input().split())) for _ in range(4)]
    length = sorted([(coords[i][0] - coords[j][0])**2 + (coords[i][1] - coords[j][1])**2 for i,j in combinations(range(4), 2)])
    
    if (length[0] == length[1] == length[2] == length[3]) and (length[4] == length[5]):
        print(1)
    else:
        print(0)