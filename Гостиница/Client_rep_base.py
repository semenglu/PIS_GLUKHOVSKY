import json
import yaml
import uuid
from abc import ABC, abstractmethod


class ClientRepBase(ABC):
    
    def __init__(self, file_path: str, strategy: StudentStrategy):
        self.file_path = file_path

    def __init__(self, strategy: StudentStrategy):
        self._data = []
        self.strategy = strategy
        self.data = self.strategy.load(self.file_path)
        self.load_data()

    @abstractmethod
    def _load_data(self):
        self.strategy.load(self.data)

    @abstractmethod
    def _save_data(self):
        self.data = self.strategy.save()

    def read_all(self):
        return self.data


    def get_all(self) -> list:
        return self.data

    def get_by_id(self, client_id):
        return next((entity for entity in self.data if entity.client_id == client_id), None)

    def get_k_n_short_list(self, k, n):
        return self.data[(n - 1) * k:n * k]

    def sort_by_field(self, field_name):
        if not hasattr(MyEntity, field_name):
            raise ValueError(f"Поле '{field_name}' не существует в сущности")
        self.data.sort(key=lambda entity: getattr(entity, field_name))

    def add_student(self, client: Client):
        client_dict = client.to_dict()
        clients = [Client.create_from_dict(client) for client in self.data]
        if not self.check_unique_code(client, clients):
            raise ValueError(f"Клиент уже существует.")
        self.data.append(client_dict)

    def check_unique_code(self, client, clients):
        for client_data in clients:
            if client_data == client:
                 raise ValueError(f"Клиент уже существует.")
        return True

    def replace_entity(self, client_id, new_entity):
        index = next((index for index, entity in enumerate(self.data) if entity.client_id == client_id), None)
        if index is not None:
            self.data[index] = new_entity
            self._save_data()
        else:
            raise ValueError(f"Элемент с ID {client_id} не найден")

    def delete_entity(self, client_id):
        self.data = [entity for entity in self.data if entity.client_id != client_id]
        self._save_data()

    def get_count(self):
        return len(self.data)