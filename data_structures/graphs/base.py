from abc import ABC, abstractmethod
from collections import defaultdict
from typing import List


class DirectedGraphBase:
    def __init__(self):
        self.adjacency_list = defaultdict(
            list
        )  # List of tuples with node and edge value

    @abstractmethod
    def add_edge(self, src: str, dest: str, value: int) -> None:
        pass

    @abstractmethod
    def bfs(self, src: str) -> List[str]:
        pass

    @abstractmethod
    def dfs(self, src: str) -> List[str]:
        pass

    @abstractmethod
    def dijkstra(self, src: str, dest: str) -> List[str]:
        pass

    @abstractmethod
    def save_to_disk(self):
        pass

    @abstractmethod
    def load_from_disk(self):
        pass
