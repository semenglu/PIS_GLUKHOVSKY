 def _load_data(self):
        """Загружает данные из файла YAML"""
        try:
            with open(self.filename, "r", encoding="utf-8") as file:
                return [MyEntity.from_dict(item) for item in yaml.safe_load(file)]
        except (FileNotFoundError, yaml.YAMLError):
            return []

    def _save_data(self):
        """Сохраняет данные в файл YAML"""
        with open(self.filename, "w", encoding="utf-8") as file:
            yaml.dump([entity.to_dict() for entity in self.data], file, allow_unicode=True)