import sys
input = sys.stdin.readline

n = int(input())

if n in set([1,3]):
    print(-1)
    sys.exit(0)
if n in set([2,4]):
    print(n//2)
    sys.exit(0)
    
num_5, remains = divmod(n,5)
if remains % 2:
    num_5, remains = num_5-1, remains+5 
num_2 = remains // 2
print(num_5+num_2)