import sys
input = sys.stdin.readline

company = set()
for _ in range(int(input())):
    name, com = input().split()
    if com == 'enter':
        company.add(name)
    else:
        company.remove(name)
print(' \n'.join(sorted(company, reverse=True)))