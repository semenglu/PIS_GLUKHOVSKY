import json
import yaml
import uuid
from abc import ABC, abstractmethod


class ClientRepBase(ABC):
    

    def __init__(self, strategy: StudentStrategy):
        self._data = []
        self.strategy = strategy
        self.load_data()

    def load(self):
        self.strategy.load(self.data)

    def save(self):
        self.data = self.strategy.save()

    def get_all(self) -> list:
        return self.data

    def get_by_id(self, client_id: int) -> dict:
            for client in self.data:
                if client.get("id") == client_id:
                    return client
            raise ValueError(f"Объект с ID {client_id} не найден.")

    def get_k_n_short_list(self, k, n):
        return self.data[(n - 1) * k:n * k]

    def sort_by_field(self, field_name):
        if not hasattr(ClientRepBase, field_name):
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

    def replace_by_id(self, client_id: int, first_name=None, last_name=None, patronymic=None, phone=None):
        client = self.get_by_id(client_id)
        if not client:
            raise ValueError(f"Клиент с ID {student_id} не найден.")
        Сlients = [Client.create_from_dict(client) for client in self._data]
        if not self.check_unique_code(client, clients):
            raise ValueError(f"Клиент уже существует.")
        if first_name:
            client.first_name = first_name
        if last_name:
            client.last_name = last_name
        if patronymic:
            client.patronymic = patronymic
        if phone:
            client.phone = phone

        for i, p in enumerate(self.data):
            if p['client_id'] == client_id:
                self.data[i] = client.to_dict()
                break
        

    def delete_entity(self, client_id):
        client = self.get_by_id(client)
        if not client:
            raise ValueError(f"Клиент с ID {client_id} не найден.")
        self.data = [p for p in self.data if p['client_id'] != client_id]

    def get_count(self):
        return len(self.data)