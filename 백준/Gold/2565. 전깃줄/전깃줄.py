import sys
input = sys.stdin.readline

lst = []
for _ in range(N := int(input())):
    lst.append(tuple(map(int, input().split())))
    
lst = [0] + [i[1] for i in sorted(lst, key = lambda x: x[0])]
dp_table = [0]

for i in range(1, N+1):
    dp_table.append(max([j for idx, j in enumerate(dp_table[:i]) if lst[idx] < lst[i]])+1)

print(N - max(dp_table))
