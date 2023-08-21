import math
import sys

input = sys.stdin.readline

for _ in range(int(input())):
    print(math.comb(*list(map(int, input().split()))[::-1]))