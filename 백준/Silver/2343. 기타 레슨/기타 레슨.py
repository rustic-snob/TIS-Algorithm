# 1    2    3    4    5    6    7    8    9
# 1    3    6    10   15   21   28   36   45

from itertools import accumulate

N, M = map(int,input().split())
lectures = list((map(int,input().split())))

l = max(lectures)
r = sum(lectures)

while l<=r:
    m = (l+r)//2
    cur = 0
    dvd = 1
    for i in lectures:
        cur += i
        if cur <= m:
           pass 
        else:
            cur = i
            dvd += 1
    if dvd <= M:
        r = m-1
        answer = m
    else:
        l = m+1
        
print(answer)

