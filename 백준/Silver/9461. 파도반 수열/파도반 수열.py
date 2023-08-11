dp_table = [0, 1, 1, 1]

for i in range(4, 101):
    dp_table.append(dp_table[i-3]+dp_table[i-2])

for _ in range(int(input())):
    print(dp_table[int(input())])