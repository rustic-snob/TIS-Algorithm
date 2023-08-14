N = int(input())

ans = [elem for s, elem in zip(map(int, input().split()), map(int, input().split())) if not s][::-1]

_ = input()

new = list(map(int, input().split()))

print(' '.join(map(str, (ans+new)[:len(new)])))