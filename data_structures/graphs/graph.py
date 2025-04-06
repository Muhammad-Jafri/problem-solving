from data_structures.graphs.base import DirectedGraphBase
from typing import List
import pickle


class Graph(DirectedGraphBase):
    def __init__(self):
        super().__init__()

    def add_edge(self, src, dest, value):
        tup = (dest, value)
        self.adjacency_list[src].append(tup)

    def bfs(self, src: str) -> List[str]:
        visited = set()  # Set object doesn't maintain order of insertion lmao
        bfs_nodes = []
        next_to_explore = [src]
        visited.add(src)
        bfs_nodes.append(src)

        while next_to_explore:
            current_node = next_to_explore.pop(0)

            for dest, _ in self.adjacency_list[current_node]:
                if dest not in visited:
                    next_to_explore.append(dest)
                    visited.add(dest)
                    bfs_nodes.append(dest)

        return bfs_nodes

    def dfs(self, src: str) -> List[str]:
        visited = set()
        traversal_order = []

        def dfs_helper(node):
            visited.add(node)
            traversal_order.append(node)

            for neighbor, _ in self.adjacency_list[node]:
                if neighbor not in visited:
                    dfs_helper(neighbor)

        dfs_helper(src)
        return traversal_order

    def dijkstra(self, src: str, dest: str) -> List[str]:
        # Find all nodes in the graph (both sources and destinations)
        all_nodes = set(self.adjacency_list.keys())
        for node in self.adjacency_list:
            for neighbor, _ in self.adjacency_list[node]:
                all_nodes.add(neighbor)
        
        # Initialize distances with infinity for all nodes except source
        distances = {node: float('infinity') for node in all_nodes}
        distances[src] = 0
        
        # Dictionary to track the previous node in optimal path
        previous = {node: None for node in all_nodes}
        
        # Priority queue
        unvisited = set(all_nodes)
        
        while unvisited:
            # Find the unvisited node with minimum distance
            current = min(unvisited, key=lambda node: distances[node])
            
            # If we reached destination or current distance is infinity (unreachable)
            if current == dest or distances[current] == float('infinity'):
                break
                
            # Remove current from unvisited
            unvisited.remove(current)
            
            # Check all neighbors of current
            for neighbor, weight in self.adjacency_list.get(current, []):
                if neighbor in unvisited:
                    # Calculate potential new distance
                    alt_distance = distances[current] + weight
                    
                    # If new distance is shorter, update distance and previous
                    if alt_distance < distances[neighbor]:
                        distances[neighbor] = alt_distance
                        previous[neighbor] = current
        
        # Reconstruct the path from dest to src
        path = []
        current = dest
        
        # If destination is unreachable
        if dest not in previous or (previous[dest] is None and dest != src):
            return path
            
        # Build path backwards from dest to src
        while current:
            path.append(current)
            current = previous[current]
        
        # Return path in the correct order (src to dest)
        return path[::-1]

    def save_to_disk(self, filename="data.pkl"):
        with open(filename, "wb") as file:
            pickle.dump(self.adjacency_list, file)

    def load_from_disk(self, filename="data.pkl"):
        with open(filename, "rb") as file:
            self.adjacency_list = pickle.load(file)


if __name__ == "__main__":
    graph = Graph()

    # Adding 5 nodes with weighted edges
    graph.add_edge("A", "B", 5)
    graph.add_edge("A", "C", 3)
    graph.add_edge("B", "D", 2)
    graph.add_edge("C", "B", 1)
    graph.add_edge("C", "E", 6)
    graph.add_edge("D", "E", 4)
    graph.add_edge("E", "A", 7)

    # Print the adjacency list to verify
    print("Graph adjacency list:")
    for node, edges in graph.adjacency_list.items():
        print(f"{node}: {edges}")

    # Run BFS starting from node A
    print("\nBFS traversal starting from A:")
    print(graph.dfs("A"))

    # Save the graph to disk
    graph.save_to_disk("example_graph.pkl")
    print("\nGraph saved to disk as 'example_graph.pkl'")
