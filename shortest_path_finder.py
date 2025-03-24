import heapq
import numpy as np
import networkx as nx

def create_graph(nodes=1000000, edges=5000000):
    graph = nx.gnm_random_graph(nodes, edges, directed=True)
    for u, v in graph.edges():
        graph[u][v]['w'] = np.random.randint(1, 20)
    return graph

def find_shortest_path(graph, start=0):
    n = graph.number_of_nodes()
    distance = {node: float('inf') for node in graph.nodes()}
    distance[start] = 0
    
    heap = [(0, start)]
    while heap:
        current_dist, current_node = heapq.heappop(heap)
        
        if current_dist > distance[current_node]:
            continue
        
        for neighbor in graph.neighbors(current_node):
            weight = graph[current_node][neighbor]['w']
            new_dist = current_dist + weight
            
            if new_dist < distance[neighbor]:
                distance[neighbor] = new_dist
                heapq.heappush(heap, (new_dist, neighbor))
    
    return distance

my_graph = create_graph(1000000, 5000000)
result = find_shortest_path(my_graph, 0)

for i in range(10):
    print(f"Shortest distance to node {i}: {result[i]}")
