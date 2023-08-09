formula = input()
sym = '+'
ans = 0
stack = []

for char in formula+'/':
    if char.isdigit():
        stack.append(char)
    elif sym == '+':
        ans += int(''.join(stack))
        sym = char
        stack = []
    else:
        ans -= int(''.join(stack))
        stack = []
        
print(ans)