# def astar(start, goal, h):
#     open_list = [start]
#     closed_list = []
#     g = {start: 0}
#     f = {start: h(start, goal)}
#     came_from = {}

#     while open_list:
#         current = min(open_list, key=lambda x: f[x])
#         if current == goal:
#             return reconstruct_path(came_from, start, goal)
#         open_list.remove(current)
#         closed_list.append(current)


#         for neighbor in get_neighbors(current):
#             tentative_g = g[current] + cost(current, neighbor)
#             if neighbor in closed_list and tentative_g >= g[neighbor]:
#                 continue
#             if neighbor not in open_list or tentative_g < g[neighbor]:
#                 came_from[neighbor] = current
#                 g[neighbor] = tentative_g
#                 f[neighbor] = tentative_g + h(neighbor, goal)
    
#                 if neighbor not in open_list:
#                     open_list.append(neighbor)
#     return None


# def reconstruct_path(came_from, start, goal):
#     path = [goal]
#     current = goal
#     while current != start:
#         current = came_from[current]
#         path.append(current)
#     path.reverse()
#     return path

# graph = {
#     'A': [('B', 3), ('D', 2)],
#     'B': [('A', 3), ('C', 4), ('D', 1)],
#     'C': [('B', 4), ('D', 5), ('E', 6)],
#     'D': [('A', 2), ('B', 1), ('C', 5), ('E', 7)],
#     'E': [('C', 6), ('D', 7)],
#     'F':[]
# }

# def get_neighbors(node):
#     return [n[0] for n in graph[node]]

# def cost(node1, node2):
#     return next(n[1] for n in graph[node1] if n[0] == node2)

# def heuristic(node, goal):
#     return 0 


# print("-----------A* Algorithm-----------")
# start = input("Enter start node : ")
# goal = input("Enter end node : ")
# print("--------------------------------------")
# path = astar(start, goal, heuristic)

# if path:
#     print("Shortest path from", start, "to", goal, ":", path)
#     total_cost = sum(cost(path[i], path[i+1]) for i in range(len(path)-1))
#     print("Total cost:", total_cost)
#     print("--------------------------------------")
# else:
#     print("There is no path from", start, "to", goal)
#     print("--------------------------------------")


def aStarAlgo(start_node, stop_node):
         
        open_set = set(start_node)
        closed_set = set()
        g = {} 
        parents = {}
       
        g[start_node] = 0
        parents[start_node] = start_node
         
         
        while len(open_set) > 0:
            n = None

            for v in open_set:
                if n == None or g[v] + heuristic(v) < g[n] + heuristic(n):
                    n = v
             
                     
            if n == stop_node or Graph_nodes[n] == None:
                pass
            else:
                for (m, weight) in get_neighbors(n):

                    if m not in open_set and m not in closed_set:
                        open_set.add(m)
                        parents[m] = n
                        g[m] = g[n] + weight
 
                    else:
                        if g[m] > g[n] + weight:
                       
                            g[m] = g[n] + weight
                           
                            parents[m] = n
                   
                            if m in closed_set:
                                closed_set.remove(m)
                                open_set.add(m)
 
            if n == None:
                print('Path does not exist!')
                return None

            if n == stop_node:
                path = []
 
                while parents[n] != n:
                    path.append(n)
                    n = parents[n]
 
                path.append(start_node)
 
                path.reverse()
 
                print('Path found: {}'.format(path))
                return path
 
            open_set.remove(n)
            closed_set.add(n)
 
        print('Path does not exist!')
        return None

def get_neighbors(v):
    if v in Graph_nodes:
        return Graph_nodes[v]
    else:
        return None

def heuristic(n):
        # H_dist = {
        #     'A': 10,
        #     'B': 8,
        #     'C': 5,
        #     'D': 7,
        #     'E': 3,
        #     'J': 0,
        #     'I': 1,
        #     'F': 6,
        #     'H': 3,
        #     'G': 5,
             
        # }
        H_dist = {
            'A': 8,
            'B': 5,
            'C': 3,
            'D': 0,
        }
 
        return H_dist[n]
 
#Describe your graph here  
# Graph_nodes = {
#     'A': [('B', 6), ('F', 3)],
#     'B': [('C', 3),('D', 2)],
#     'C': [('D', 1),('E', 5)],
#     'D': [('E', 8)],
#     'E': [('I', 5),('J', 5)],
#     'J': [('I', 3)],
#     'I': [('G', 3),('H', 2)],
#     'G': [('F', 1)],
#     'H': [('F', 7)],
#     'F': None
     
# }
Graph_nodes = {
    'A': [('B', 1), ('C', 2), ('D', 7)],
    'B': [('C', 3)],
    'C': [('D', 2)],
    'D':None 
}
aStarAlgo('A', 'D')