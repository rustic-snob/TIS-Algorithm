def euclid_lcm(A, B):
    if A < B:
        n, m = B, A
    else:
        n, m = A, B
    while m:
        n, m = m, n % m
    return A * B // n
        
print(euclid_lcm(*map(int, input().split())))