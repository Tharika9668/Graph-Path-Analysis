import heapq
import networkx as nx

def read_graph(file_path):
    graph = nx.DiGraph()
    with open(file_path, 'r') as file:
        for line in file:
            if not line.startswith('#'):
                src, dest = map(int, line.split()[:2])
                graph.add_edge(src, dest, weight=1)
    print(f"Graph has {graph.number_of_nodes()} nodes and {graph.number_of_edges()} edges.")
    return graph

def shortest_path(graph, start_node=0):
    if start_node not in graph:
        print("Node 0 not found. Using a random node as the source.")
        start_node = list(graph.nodes())[0]

    distances = {node: float('inf') for node in graph.nodes()}
    distances[start_node] = 0
    
    priority_queue = [(0, start_node)]
    while priority_queue:
        curr_dist, curr_node = heapq.heappop(priority_queue)
        if curr_dist > distances[curr_node]:
            continue
        for neighbor in graph.neighbors(curr_node):
            weight = graph[curr_node][neighbor].get('weight', 1)
            total_dist = curr_dist + weight
            if total_dist < distances[neighbor]:
                distances[neighbor] = total_dist
                heapq.heappush(priority_queue, (total_dist, neighbor))
    
    return distances

graph_path = '/Users/tharikaganesan/Downloads/ca-HepPh.txt'
graph = read_graph(graph_path)
result = shortest_path(graph)

output_path = '/Users/tharikaganesan/Downloads/output.txt'
with open(output_path, 'w') as output_file:
    for i in range(10):
        output_file.write(f"Shortest distance to node {i}: {result.get(i, 'Not reachable')}\n")
    print(f"Output saved to {output_path}")
