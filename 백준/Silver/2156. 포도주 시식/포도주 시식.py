## t-2, t-1 모두 마시지 않아도 된다는 점에서 2579와 다름
## (모두스킵 , t-1스킵, t-2스킵)
## (max(dp_table[i-3]),
##  max(dp_table[i-2]), 
##  max(dp_table[i-1][:2]))

import sys
input = sys.stdin.readline

wines = [0,0]
dp_table = [(0,0,0), (0,0,0)]

for i in range(2, int(input())+2):
    wines.append(wine:=int(input()))
    dp_table.append((max(dp_table[i-3])+wine,
                     max(dp_table[i-2])+wine, 
                     max(dp_table[i-1][:2])+wine))
    
print(max(max(dp_table[-2]), max(dp_table[-1])))