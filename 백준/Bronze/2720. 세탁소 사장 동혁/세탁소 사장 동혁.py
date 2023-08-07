import sys
input = sys.stdin.readline

order = [25, 10, 5]

for _ in range(int(input())):
    cashier = []
    money = int(input())
    
    for i in order:
        remains, money = divmod(money, i)
        cashier.append(remains)
    
    cashier.append(money)
        
    print(' '.join(map(str, cashier)))