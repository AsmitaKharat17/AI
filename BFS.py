graph = {
  'A' : ['B','C'],
  'B' : ['D', 'E'],
  'C' : ['G'],
  'D' : [],
  'E' : ['F'],
  'F' : [],
  'G' : []
}

visited = [] 
queue = []     

def bfs(visited, graph, node): 
  visited.append(node)
  queue.append(node)

  while queue:          
     print(queue)
     m = queue.pop(0) 

     for neighbour in graph[m]:
      if neighbour not in visited:
        visited.append(neighbour)
        queue.append(neighbour)
       
  print(queue)

print("Following is the Breadth-First Search:")
bfs(visited, graph, 'A')
