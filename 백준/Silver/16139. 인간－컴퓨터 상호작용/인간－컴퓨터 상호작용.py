import sys
input = sys.stdin.readline

from collections import defaultdict

S = input().strip()
acc_dict = defaultdict(lambda: [0])

for char_in_string in S:
    for ord_in_dict in range(ord('a'), ord('z')+1):
        if char_in_string == (char_in_dict:=chr(ord_in_dict)):
            acc_dict[char_in_dict].append(acc_dict[char_in_dict][-1]+1)
        else:
            acc_dict[char_in_dict].append(acc_dict[char_in_dict][-1])

for _ in range(int(input())):
    alpha, start, end = input().split()
    start, end = int(start), int(end)
    
    print(acc_dict[alpha][end+1] - acc_dict[alpha][start])