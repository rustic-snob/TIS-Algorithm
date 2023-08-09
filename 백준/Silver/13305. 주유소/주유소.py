N = int(input())
roads = map(int, input().split())
gases = map(int, input().split()[:-1])

opt_gas = float('inf')
ans = 0

for road, gas in zip(roads, gases):
    if gas < opt_gas:
        opt_gas = gas
    ans += opt_gas * road
    
print(ans)