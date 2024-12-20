from abc import ABC, abstractmethod
from typing import List


class ClientStrategy(ABC):

    @abstractmethod
    def load(self, file_path: str) -> List[dict]:
        pass

    @abstractmethod
    def save(self, file_path: str, data: List[dict]):
        pass

    @abstractmethod
    def display(self):
        pass