import json
import yaml
import uuid
from abc import ABC, abstractmethod


class MyEntityRepBase(ABC):
    """Базовый класс для репозиториев, работающих с данными (общая логика)"""
    
    def __init__(self, filename: str):
        self.filename = filename
        self.data = self._load_data()

    @abstractmethod
    def _load_data(self):
        """Загружает данные из файла"""
        pass

    @abstractmethod
    def _save_data(self):
        """Сохраняет данные в файл"""
        pass

    def read_all(self):
        """Чтение всех значений из файла"""
        return self.data

    def write_all(self):
        """Запись всех значений в файл"""
        self._save_data()

    def get_by_id(self, client_id):
        """Получить объект по ID"""
        return next((entity for entity in self.data if entity.client_id == client_id), None)

    def get_k_n_short_list(self, k, n):
        """Получить список k по счету n объектов (например, вторые 20 элементов)"""
        return self.data[(n - 1) * k:n * k]

    def sort_by_field(self, field_name):
        """Сортировка элементов по выбранному полю"""
        if not hasattr(MyEntity, field_name):
            raise ValueError(f"Поле '{field_name}' не существует в сущности")
        self.data.sort(key=lambda entity: getattr(entity, field_name))

    def add_entity(self, entity):
        """Добавить объект в список (сформировать новый ID)"""
        entity.client_id = uuid.uuid4().int  # Генерация уникального ID
        self.data.append(entity)
        self._save_data()

    def replace_entity(self, client_id, new_entity):
        """Заменить элемент списка по ID"""
        index = next((index for index, entity in enumerate(self.data) if entity.client_id == client_id), None)
        if index is not None:
            self.data[index] = new_entity
            self._save_data()
        else:
            raise ValueError(f"Элемент с ID {client_id} не найден")

    def delete_entity(self, client_id):
        """Удалить элемент списка по ID"""
        self.data = [entity for entity in self.data if entity.client_id != client_id]
        self._save_data()

    def get_count(self):
        """Получить количество элементов"""
        return len(self.data)