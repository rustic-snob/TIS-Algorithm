def rsum(R):
    return sum([int(i) * 4**(len(bin(R)[2:]) - idx - 1) for idx, i in enumerate(bin(R)[2:])]) * 2
def csum(C):
    return sum([int(i) * 4**(len(bin(C)[2:]) - idx - 1) for idx, i in enumerate(bin(C)[2:])])

_, R, C = map(int, input().split())

print(rsum(R)+csum(C))