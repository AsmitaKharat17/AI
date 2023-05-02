# graph = {
#   'A' : ['B','C'],
#   'B' : ['D', 'E'],
#   'C' : ['G'],
#   'D' : [],
#   'E' : ['F'],
#   'F' : [],
#   'G' : []
# }

# visited = [] 
# queue = []     

# def bfs(visited, graph, node): 
#   visited.append(node)
#   queue.append(node)

#   while queue:          
#      print(queue)
#      m = queue.pop(0) 

#      for neighbour in graph[m]:
#       if neighbour not in visited:
#         visited.append(neighbour)
#         queue.append(neighbour)
       
#   print(queue)

# print("Following is the Breadth-First Search")
# bfs(visited, graph, 'A')

# --------------------------------------------------------------------------------------


from collections import deque

class Graph:
    def __init__(self, directed=True):
        self.edges = {}
        self.directed = directed

    def add_edge(self, node1, node2, __reversed=False):
        try: neighbors = self.edges[node1]
        except KeyError: neighbors = set()
        neighbors.add(node2)
        self.edges[node1] = neighbors
        if not self.directed and not __reversed: self.add_edge(node2, node1, True)

    def neighbors(self, node):
        try: return self.edges[node]
        except KeyError: return []

    def breadth_first_search(self, start, goal):
        found, fringe, visited, came_from = False, deque([start]), set([start]), {start: None}
        print('{:11s} | {}'.format('Expand Node', 'Fringe'))
        print('--------------------')
        print('{:11s} | {}'.format('-', start))
        while not found and len(fringe):
            current = fringe.pop()
            print('{:11s}'.format(current), end=' | ')
            if current == goal: found = True; break
            for node in self.neighbors(current):
                if node not in visited: visited.add(node); fringe.appendleft(node); came_from[node] = current
            print(', '.join(fringe))
        if found: print(); return came_from
        else: print('No path from {} to {}'.format(start, goal))

    @staticmethod
    def print_path(came_from, goal):
        parent = came_from[goal]
        if parent:
            Graph.print_path(came_from, parent)
        else: print(goal, end='');return
        print(' =>', goal, end='')


    def __str__(self):
        return str(self.edges)


graph = Graph(directed=False)
graph.add_edge('A', 'B')
graph.add_edge('A', 'S')
graph.add_edge('S', 'G')
graph.add_edge('S', 'C')
graph.add_edge('C', 'F')
graph.add_edge('G', 'F')
graph.add_edge('C', 'D')
graph.add_edge('C', 'E')
graph.add_edge('E', 'H')
graph.add_edge('G', 'H')
start, goal = 'A', 'H'
traced_path = graph.breadth_first_search(start, goal)
if (traced_path): print('Path:', end=' '); Graph.print_path(traced_path, goal);print()

----------------------------------------------------------------
# import dictionary for graph
from collections import defaultdict

# function for adding edge to graph
graph = defaultdict(list)
def addEdge(graph,u,v):
	graph[u].append(v)

def generate_edges(graph):
	edges = []
 
	for node in graph:
		for neighbour in graph[node]:
			
			# if edge exists then append
			edges.append((node, neighbour))
	return edges

# declaration of graph as dictionary
print("\nInput tree nodes. Press 0 to end input\n")
parent=1
while not (parent==0):
    parent=int(input("Enter parent node: "))
    child=int(input("Enter child node: "))
    if parent==0 and child==0:
        break
    addEdge(graph,parent,child)


# Driver Function 
print(generate_edges(graph))
visited = [] # List for visited nodes.
queue = []     #Initialize a queue

def bfs(visited, graph, node): 
  k=1
  visited.append(node)
  queue.append(node)
  

  while queue:          
    m = queue.pop(0) 

    for neighbour in graph[m]:
      if neighbour not in visited:
        visited.append(neighbour)
        queue.append(neighbour)
        print("Iteration ",k)
        print("Visited: ",visited)
        print("Queue: ",queue)
        print("\n")
        k=k+1

start=int(input("\nWhat is the starting node?: "))

print("\nFollowing is the Breadth-First Search\n")
bfs(visited, graph, start)    


# input tree: use if input not given 
# parent: 1
# child: 2
# p:1
# c:3
# p:2
# c:4
# p:2
# c:5
# p:3
# c:6
# p:5
# c:6
# once all nodes are entered, enter p:0 and c:0 to start DFS
# start node: 1