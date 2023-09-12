import sys
import heapq

input = sys.stdin.readline

min_heap = []
max_heap = []

for _ in range(int(input())):
    if len(min_heap) == len(max_heap):
        heapq.heappush(max_heap, -int(input()))
    else:
        heapq.heappush(min_heap, int(input()))
        
    if min_heap and min_heap[0] < -max_heap[0]:
        i = heapq.heappop(max_heap)
        j = heapq.heappop(min_heap)
        
        heapq.heappush(min_heap, -i)
        heapq.heappush(max_heap, -j)
    
    print(-max_heap[0])
    