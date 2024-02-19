import collections
import heapq

class graph:
   def __init__(self,gdict=None):
      if gdict is None:
         gdict = {}
      self.gdict = gdict
# Check for the visisted and unvisited nodes
def dfs(graph, start, visited = None):
   if visited is None:
      visited = set()
   visited.add(start)
   print(start)
   for next in graph[start] - visited:
      dfs(graph, next, visited)
   return visited

gdict = { 
   "a" : set(["b","c"]),
   "b" : set(["a", "d"]),
   "c" : set(["a", "d"]),
   "d" : set(["e"]),
   "e" : set(["a"])
}


class graph:
   def __init__(self,gdict=None):
      if gdict is None:
         gdict = {}
      self.gdict = gdict
def bfs(graph, startnode):
# Track the visited and unvisited nodes using queue
   seen, queue = set([startnode]), collections.deque([startnode])
   while queue:
      vertex = queue.popleft()
      marked(vertex)
      for node in graph[vertex]:
         if node not in seen:
            seen.add(node)
            queue.append(node)

def marked(n):
   print(n)

# The graph dictionary
gdict = { 
   "a" : set(["b","c"]),
   "b" : set(["a", "d"]),
   "c" : set(["a", "d"]),
   "d" : set(["e"]),
   "e" : set(["a"])
}


#Dijkstra

def dijkstra(graph,node):    
    distances={node:float('inf') for node in graph}
    distances[node]=0
    came_from={node:None for node in graph}    
    queue=[(0,node)]
    
    while queue:
        current_distance,current_node=heapq.heappop(queue)
        # relaxation
        for next_node,weight in graph[current_node].items():
            distance_temp=current_distance+weight
            if distance_temp<distances[next_node]:
                distances[next_node]=distance_temp
                came_from[next_node]=current_node
                heapq.heappush(queue,(distance_temp,next_node))
    return distances,came_from
#A*
def astar(graph,start_node,end_node):
   
    f_distance={node:float('inf') for node in graph}
    f_distance[start_node]=0
    
    g_distance={node:float('inf') for node in graph}
    g_distance[start_node]=0
    
    came_from={node:None for node in graph}
    came_from[start_node]=start_node
    
    queue=[(0,start_node)]    
    while queue:
        current_f_distance,current_node=heapq.heappop(queue)

        if current_node == end_node:
            return f_distance, came_from
        for next_node,weights in graph[current_node].items():               
            temp_g_distance=g_distance[current_node]+weights[0]            
            if temp_g_distance<g_distance[next_node]:                
                g_distance[next_node]=temp_g_distance
                heuristic=weights[1]                
                f_distance[next_node]=temp_g_distance+heuristic
                came_from[next_node]=current_node
                
                heapq.heappush(queue,(f_distance[next_node],next_node))
    return f_distance, came_from


print("Breath first serach\n")
bfs(gdict, "a")
print("\nDepth first serach\n")
dfs(gdict, 'a')