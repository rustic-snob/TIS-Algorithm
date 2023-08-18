_ = input()
nums = set(map(int, input().split()))
_ = input()
for i in map(int, input().split()):
    if i in nums:
        print(1)
    else:
        print(0)