## QUESTION: https://www.hackerrank.com/challenges/ctci-bfs-shortest-reach/problem
from collections import defaultdict

class Graph:
    def __init__(self,n):
        self.graph = defaultdict(list)
        self.numNodes = n
    
    def connect(self,x,y):
        self.graph[x].append(y)
        self.graph[y].append(x)
    
    def find_all_distances(self,s):
        distance = [-1]*self.numNodes
        visited = [0]*self.numNodes
        queue = []
        queue.append(s)
        visited[s] = 1
        distance[s] = 0
        while queue:
            curr = queue.pop(0)
            for i in self.graph[curr]: 
                tempDist = 0
                if (visited[i] == 0):
                    tempDist =distance[curr] + 6
                    distance[i] = tempDist
                    queue.append(i)
                    visited[i] = 1
       
        ## remove all 0 values from list
        distance = list(filter(lambda a: a!=0, distance))
        print(*distance)
        # for i in distance:
        #     if (i != 0):
        #         print()
        
t = int(input())
for i in range(t):
    n,m = [int(value) for value in input().split()]
    # inp = list(map(int,input().split()))
    # n,m = inp[0], inp[1]
    graph = Graph(n)
    for i in range(m):
        x,y = [int(x) for x in input().split()]
        graph.connect(x-1,y-1)
    s = int(input())
    graph.find_all_distances(s-1)
