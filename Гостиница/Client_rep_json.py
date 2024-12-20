import json
import os


class ClientRepJson(ClientStrategy):

    def load(self, file_path: str) -> List[dict]:
        try:
            with open(file_path, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    def save(self, file_path: str, data: List[dict]):
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)

    def display(self, file_path: str):
       data = self.load(file_path)
       for item in data:
            print(item)