# 1 -> 1
# 2 -> 2 
# 3 -> 2 
# 4 -> 4
# 5 -> 2 
# 6 -> 4
# 7 -> 6
# 8 -> 8
# 9 -> 2
# 10 -> 4

def card(nums, drop_first):
    if len(nums) == 1:
        return nums[0]
    if (len(nums)%2 and drop_first):
        return card(nums[1::2], False)
    elif (len(nums)%2 and not drop_first):
        return card(nums[::2], True)
    elif (not len(nums)%2 and drop_first):
        return card(nums[1::2], True)
    else:
        return card(nums[::2], False)

N = int(input())
if N == 1:
    print(1)
else:
    print(card([i for i in range(1, N+1)], True))


        
    