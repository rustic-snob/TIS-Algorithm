import sys
input = sys.stdin.readline

infected = set(['ChongChong'])

for _ in range(int(input())):
    vertices = input().split()
    if vertices[0] in infected:
        infected.add(vertices[1])
    elif vertices[1] in infected:
        infected.add(vertices[0])
        
print(len(infected))
        