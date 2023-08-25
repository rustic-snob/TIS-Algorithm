import sys

N, K = map(int, input().split())
binary = bin(N)

if binary.count('1') <= K:
    print(0)

else:        
    ans = 0
    
    while binary.count('1') > K:
        ans += int((2**(len(binary) - binary.rfind('1')-1)))
        binary = bin(int(binary, 2) + int((2**(len(binary) - binary.rfind('1')-1))))

    print(ans)

