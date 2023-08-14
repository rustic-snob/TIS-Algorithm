import sys
input = sys.stdin.readline

def cantor(dashes):
    return dashes + ' '*len(dashes) + dashes

try:
    while True:
        dashes = '-'
        N = int(input())
        while N:
            dashes = cantor(dashes)
            N -= 1
        print(dashes)
        
except:
    sys.exit(0)

