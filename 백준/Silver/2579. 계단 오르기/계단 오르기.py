# t번째 계단까지 두 가지 값을 memo:
# t-2번째 계단까지의 두 가지 값 중 max + t
# t-1번째 계단까지의 두 가지 값 중 t-2를 거치지 않은 값 + t

# [0      | 0      | 0      | 0      | 0      | 0     ]
# [10, 10 | 0      | 0      | 0      | 0      | 0     ]
# [10, 10 | 20, 30 | 0      | 0      | 0      | 0     ]
# [10, 10 | 20, 30 | 25, 35 | 0      | 0      | 0     ]
# [10, 10 | 20, 30 | 25, 35 | 55, 50 | 0      | 0     ]
# [10, 10 | 20, 30 | 25, 35 | 55, 50 | 45, 65 | 0     ]
# [10, 10 | 20, 30 | 25, 35 | 55, 50 | 45, 65 | 75, 65]

import sys
input = sys.stdin.readline

steps = [0,0]
dp_table = [(0,0), (0,0)]

for i in range(2, int(input())+2):
    steps.append(step:=int(input()))
    dp_table.append((max(dp_table[i-2])+step,dp_table[i-1][0]+step))
    
print(max(dp_table[-1]))   
 