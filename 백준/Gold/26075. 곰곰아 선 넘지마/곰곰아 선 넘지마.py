from math import ceil

zeros, ones = map(int, input().split())
piv = '0' if zeros < ones else '1'
S = input()
T = input()

S_arr = [idx for idx, s in enumerate(S) if s == piv]
T_arr = [idx for idx, t in enumerate(T) if t == piv]

cnt = sum([abs(s-t) for s, t in zip(S_arr, T_arr)])

if cnt % 2:
    print((cnt//2)**2 + ((cnt//2)+1)**2)
else:
    print(((cnt//2)**2*2))



