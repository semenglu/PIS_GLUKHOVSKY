import json
import os


class MyEntity_rep_json:
    def __init__(self, filename="clients_data.json"):
        self.filename = filename
        self.data = self._load_data()

    def _load_data(self):
        """Загружает данные из файла JSON (пункт a)"""
        try:
            with open(self.filename, "r", encoding="utf-8") as file:
                return [MyEntity.from_dict(item) for item in json.load(file)]
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def _save_data(self):
        """Сохраняет данные в файл JSON (пункт b)"""
        with open(self.filename, "w", encoding="utf-8") as file:
            json.dump([entity.to_dict() for entity in self.data], file, ensure_ascii=False, indent=4)

    def read_all(self):
        """Чтение всех значений из файла (пункт a)"""
        return self.data

    def write_all(self):
        """Запись всех значений в файл (пункт b)"""
        self._save_data()

    def get_by_id(self, client_id):
        """Получить объект по ID (пункт c)"""
        return next((entity for entity in self.data if entity.client_id == client_id), None)

    def get_k_n_short_list(self, k, n):
        """Получить список k по счету n объектов (например, вторые 20 элементов) (пункт d)"""
        return self.data[(n - 1) * k:n * k]

    def sort_by_field(self, field_name):
        """Сортировка элементов по выбранному полю (пункт e)"""
        if not hasattr(MyEntity, field_name):
            raise ValueError(f"Поле '{field_name}' не существует в сущности")
        self.data.sort(key=lambda entity: getattr(entity, field_name))

    def add_entity(self, entity):
        """Добавить объект в список (сформировать новый ID) (пункт f)"""
        entity.client_id = uuid.uuid4().int  # Генерация уникального ID
        self.data.append(entity)
        self._save_data()

    def replace_entity(self, client_id, new_entity):
        """Заменить элемент списка по ID (пункт g)"""
        index = next((index for index, entity in enumerate(self.data) if entity.client_id == client_id), None)
        if index is not None:
            self.data[index] = new_entity
            self._save_data()
        else:
            raise ValueError(f"Элемент с ID {client_id} не найден")

    def delete_entity(self, client_id):
        """Удалить элемент списка по ID (пункт h)"""
        self.data = [entity for entity in self.data if entity.client_id != client_id]
        self._save_data()

    def get_count(self):
        """Получить количество элементов (пункт i)"""
        return len(self.data)