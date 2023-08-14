import sys

N = int(input())

line = list(map(int, input().split())) + [0]
obj = [0]
stack = [0]

while len(obj) != N+1:
    if line[0] == obj[-1]+1:
        obj.append(line.pop(0))
    elif stack[-1] == obj[-1]+1:
        obj.append(stack.pop())
    else:
        if len(line) == 1:
            print('Sad')
            sys.exit(0)
        stack.append(line.pop(0))
print('Nice')
    