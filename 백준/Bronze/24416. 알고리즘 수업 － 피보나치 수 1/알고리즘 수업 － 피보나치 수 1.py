lst = [0, 1, 1]

for i in range(3, 41):
    lst.append(lst[i-1]+lst[i-2])
    
n = int(input())

print(lst[n], n-2)