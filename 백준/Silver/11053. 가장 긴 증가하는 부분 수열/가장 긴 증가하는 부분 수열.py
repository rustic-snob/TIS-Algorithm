N = int(input())
A = [0] + list(map(int, input().split()))
D = [0]*(N+1)

for i in range(1, N+1):
    D[i] = max([d for idx, d in enumerate(D[:i]) if A[idx] < A[i]]) + 1

print(max(D))