from data_structures.graphs.graph import Graph
import unittest
import os


class TestGraphs(unittest.TestCase):
    def setUp(self):
        """Set up a fresh Graph before each test."""
        self.graph = Graph()

    def test_add_edge(self):
        self.graph.add_edge("A", "B", 10)
        self.assertEqual(self.graph.adjacency_list["A"], [("B", 10)])
        self.assertEqual(self.graph.adjacency_list["B"], [])

    def test_multiple_edges(self):
        self.graph.add_edge("A", "B", 5)
        self.graph.add_edge("A", "C", 3)
        self.graph.add_edge("B", "C", 2)
        self.assertEqual(len(self.graph.adjacency_list["A"]), 2)
        self.assertEqual(self.graph.adjacency_list["A"], [("B", 5), ("C", 3)])
        self.assertEqual(self.graph.adjacency_list["B"], [("C", 2)])

    def test_bfs(self):
        # Create a simple graph for testing BFS
        self.graph.add_edge("A", "B", 1)
        self.graph.add_edge("A", "C", 1)
        self.graph.add_edge("B", "D", 1)
        self.graph.add_edge("C", "D", 1)
        
        # BFS from node A should visit all nodes
        result = self.graph.bfs("A")
        self.assertEqual(len(result), 4)
        self.assertEqual(result[0], "A")  # Start node should be first
        self.assertIn("B", result)
        self.assertIn("C", result)
        self.assertIn("D", result)
        
        # BFS from node B should not visit A
        result = self.graph.bfs("B")
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0], "B")
        self.assertIn("D", result)
        self.assertNotIn("A", result)
        self.assertNotIn("C", result)

    def test_dfs(self):
        # Create a graph for testing DFS
        self.graph.add_edge("A", "B", 1)
        self.graph.add_edge("A", "C", 1)
        self.graph.add_edge("B", "D", 1)
        self.graph.add_edge("C", "D", 1)
        
        # DFS from node A
        result = self.graph.dfs("A")
        self.assertEqual(len(result), 4)
        self.assertEqual(result[0], "A")  # Start node should be first
        
        # The exact order depends on implementation but should contain all nodes
        self.assertIn("B", result)
        self.assertIn("C", result)
        self.assertIn("D", result)

    def test_dijkstra(self):
        # Create a weighted graph for testing Dijkstra
        self.graph.add_edge("A", "B", 4)
        self.graph.add_edge("A", "C", 2)
        self.graph.add_edge("B", "D", 5)
        self.graph.add_edge("C", "B", 1)
        self.graph.add_edge("C", "D", 8)
        self.graph.add_edge("C", "E", 10)
        self.graph.add_edge("D", "E", 2)
        self.graph.add_edge("D", "F", 6)
        self.graph.add_edge("E", "F", 3)
        
        # Test shortest path from A to F
        path = self.graph.dijkstra("A", "F")
        self.assertEqual(path, ["A", "C", "B", "D", "E", "F"])
        
        # Test shortest path from A to D
        path = self.graph.dijkstra("A", "D")
        self.assertEqual(path, ["A", "C", "B", "D"])
        
        # Test shortest path from A to A (should be just A)
        path = self.graph.dijkstra("A", "A")
        self.assertEqual(path, ["A"])
        
        # Test path to unreachable node
        self.graph.add_edge("G", "H", 1)  # Disconnected from other nodes
        path = self.graph.dijkstra("A", "G")
        self.assertEqual(path, [])  # Should return empty list for unreachable nodes

    # def test_save_and_load(self):
    #     # Create a graph
    #     self.graph.add_edge("A", "B", 5)
    #     self.graph.add_edge("B", "C", 3)
        
    #     # Save to disk
    #     test_filename = "test_graph.pkl"
    #     self.graph.save_to_disk(test_filename)
        
    #     # Verify file was created
    #     self.assertTrue(os.path.exists(test_filename))
        
    #     # Create a new graph instance
    #     new_graph = Graph()
        
    #     # Load from disk
    #     new_graph.load_from_disk(test_filename)
        
    #     # Verify the loaded graph is the same
    #     self.assertEqual(new_graph.adjacency_list["A"], [("B", 5)])
    #     self.assertEqual(new_graph.adjacency_list["B"], [("C", 3)])
        
    #     # Clean up
    #     os.remove(test_filename)


if __name__ == "__main__":
    unittest.main()