import os
from abc import ABC, abstractmethod

class ClientStrategy(ABC):
    @abstractmethod
    def _read_from_file(self, filename):
        pass

    @abstractmethod
    def _write_to_file(self, filename, clients):
        pass