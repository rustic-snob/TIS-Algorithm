A = ' ' + input()
B = ' ' + input()

dp_table = [[0] * (len(A)) for _ in range(len(B))]
dp_table[0] = list(range(len(A)))
for idx in range(len(B)):
    dp_table[idx][0] = idx
    
for i in range(1, len(B)):
    for j in range(1, len(A)):
        if A[j] == B[i]:
            cost = 0
        else:
            cost = 1
        dp_table[i][j] = min(dp_table[i-1][j-1]+cost,dp_table[i][j-1]+1, dp_table[i-1][j]+1)

print(dp_table[i][j])