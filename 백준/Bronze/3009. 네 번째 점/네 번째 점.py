from collections import Counter

cnt_x = Counter()
cnt_y = Counter()

for _ in range(3):
    x, y = map(int, input().split())
    cnt_x[x]+=1
    cnt_y[y]+=1
    
print(cnt_x.most_common()[-1][0], cnt_y.most_common()[-1][0])