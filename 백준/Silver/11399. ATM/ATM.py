from itertools import accumulate as a
_=input()
print(sum(a(sorted(map(int, input().split())))))