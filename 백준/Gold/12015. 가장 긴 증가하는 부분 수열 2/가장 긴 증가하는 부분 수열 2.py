import bisect

_ = input()
A = [0] + list(map(int, input().split()))
dp_table = [0]

for i, a in enumerate(A):
    if a > dp_table[-1]:
        dp_table.append(a)
    else:
        idx = bisect.bisect_left(dp_table, a)
        dp_table[idx] = a

print(len(dp_table)-1)