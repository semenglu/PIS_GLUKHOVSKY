class ClientRepJson(ClientRepBase):
    """Класс для работы с данными в формате JSON"""

    def _load_data(self):
        """Загружает данные из файла JSON"""
        try:
            with open(self.filename, "r", encoding="utf-8") as file:
                return [MyEntity.from_dict(item) for item in json.load(file)]
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def _save_data(self):
        """Сохраняет данные в файл JSON"""
        with open(self.filename, "w", encoding="utf-8") as file:
            json.dump([entity.to_dict() for entity in self.data], file, ensure_ascii=False, indent=4)
