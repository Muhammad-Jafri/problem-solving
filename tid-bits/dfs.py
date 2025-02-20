def dfs(adj_list, start):
    visited = set()
    res = []

    def dfs_wrapper(adj_list, node):
        visited.add(node)
        res.append(node)
        print(node)
        for adj_node in adj_list[node]:
            if adj_node not in visited:
                dfs_wrapper(adj_list, adj_node)

    dfs_wrapper(adj_list, start)

    return res


graph = {
    "A": ["B", "C"],
    "B": ["A", "D", "E"],
    "C": ["A", "F"],
    "D": ["B"],
    "E": ["B"],
    "F": ["C"],
}

# Start DFS from node 'A'
print(dfs(graph, "A"))
