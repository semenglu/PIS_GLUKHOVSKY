class ClientRepJson(ClientRepBase):

    def _load_data(self):
        try:
            with open(self.filename, "r", encoding="utf-8") as file:
                return [MyEntity.from_dict(item) for item in json.load(file)]
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def _save_data(self):
        with open(self.filename, "w", encoding="utf-8") as file:
            json.dump([entity.to_dict() for entity in self.data], file, ensure_ascii=False, indent=4)
