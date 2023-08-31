import sys
input = sys.stdin.readline

class Vertex():
    def __init__(self, char = None, spe = None):
        self.char = char
        self.edge = set() # 각 Vertex에 adjacent edges를 저장
        self.spe = spe
        
class MinPriorityQueue():
    def __init__(self):             
        self.heap = [None]        
        self.heap_size = 0
    
    def parent(self, i):
        return int(i / 2)
    
    def left(self, i):
        return 2 * i
    
    def right(self, i):
        return 2 * i + 1
    
    def min_heapify(self, i):
        l = self.left(i)
        r = self.right(i)
        if (l <= self.heap_size) and (self.heap[l].spe < self.heap[i].spe):
            smallest = l
        else:
            smallest = i
        if (r <= self.heap_size) and (self.heap[r].spe < self.heap[smallest].spe):
            smallest = r
        if smallest != i:
            temp = self.heap[smallest]
            self.heap[smallest] = self.heap[i]
            self.heap[i] = temp
            self.min_heapify(smallest)
    
    def extract_min(self):
        if self.heap_size < 1:
           raise Exception("heap underflow")
        if self.heap_size == 1:
            self.heap_size -= 1
            return self.heap.pop()
        else:
            min = self.heap[1]
            self.heap[1] = self.heap.pop()
            self.heap_size -= 1
            self.min_heapify(1)
            return min
    
    def decrease_key(self, i, vertex):
        if vertex.spe > self.heap[i].spe:
            raise Exception("new key must be smaller than current one")
        self.heap[i] = vertex
        while (i > 1) and self.heap[self.parent(i)].spe > self.heap[i].spe:
            temp = self.heap[self.parent(i)]
            self.heap[self.parent(i)] = self.heap[i]
            self.heap[i] = temp
            i = self.parent(i)
            
    def heap_insert(self,vertex):
        self.heap_size += 1
        inf_vertex = Vertex(spe = float('inf'))
        self.heap.append(inf_vertex)
        self.decrease_key(self.heap_size, vertex)

def initialize_single_source(graph, source):
    for vertex in graph:
        if vertex.char != source:
            vertex.spe = float('inf')
        else:
            vertex.spe = 0
            
def relax(u, v, weight, PriorityQueue):
    if v.spe > u.spe + weight[u.char][v.char]:
        v.spe = u.spe + weight[u.char][v.char]
        PriorityQueue.decrease_key(PriorityQueue.heap.index(v),v)

def dijkstra(graph, weight, source):
    initialize_single_source(graph, source)
    PriorityQueue = MinPriorityQueue()
    for vertex in graph:
        PriorityQueue.heap_insert(vertex)
    while PriorityQueue.heap_size:
        u = PriorityQueue.extract_min()
        for v in u.edge:
            v = globals()[v]
            relax(u,v,weight,PriorityQueue)

graph = []
weight = dict()

vertex, edge = input().split()
for i in range(1, int(vertex)+1):  
    globals()[str(i)] = Vertex(char = str(i))
    graph.append(globals()[str(i)])
    weight[str(i)] = dict()
    
source = input().strip()     

for _ in range(int(edge)):
    src, tgt, key = input().split(' ')
    globals()[src].edge.add(tgt)
    if tgt not in weight[src] : weight[src][tgt] = int(key)
    else : weight[src][tgt] = min(weight[src][tgt], int(key))

dijkstra(graph, weight, source)
for vertex in graph:
    if vertex.spe == float('inf'):
        print("INF")
    else:
        print(vertex.spe)