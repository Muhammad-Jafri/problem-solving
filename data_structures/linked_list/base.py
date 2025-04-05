from abc import ABC, abstractmethod
from typing import Optional, Union
from data_structures.linked_list.node import Node


class LinkedListBase(ABC):
    def __init__(self):
        self.head: Optional[Node] = None

    @abstractmethod
    def insert_at_head(self) -> None:
        pass

    @abstractmethod
    def insert_at_tail(self) -> None:
        pass

    @abstractmethod
    def count_elements(self) -> int:
        pass

    @abstractmethod
    def delete_at_head(self) -> Optional[Node]:
        pass

    @abstractmethod
    def delete_at_tail(self) -> Optional[Node]:
        pass
