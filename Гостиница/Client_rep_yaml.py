import yaml


class ClientRepYaml(ClientStrategy):
    def __init__(self, filename):
        self.filename = filename
        self.clients = self._read_from_file()

    def _read_from_file(self):
        try:
            with open(self.filename, "r") as file:
                data = yaml.safe_load(file) or []
                clients_list = []
                for item in data:
                    client = FullClient(
                        client_id=item["client_id"],
                        surname=item["surname"],
                        first_name=item["first_name"],
                        patronymic=item["patronymic"],
                        email=item["email"],
                        phone_number=item["phone_number"],
                        passport_number=item["passport_number"],
                        comment=item["comment"],
                    )
                    clients_list.append(client)
                return clients_list
        except FileNotFoundError:
            return [] 
        except yaml.YAMLError:
            return []

    def _write_to_file(self):
        data_to_write = [
            {
                "entity_id": entity.entity_id,
                "surname": entity.surname,
                "first_name": entity.first_name,
                "patronymic": entity.patronymic,
                "email": entity.email,
                "phone_number": entity.phone_number,
                "passport_number": entity.passport_number,
                "comment": entity.comment,
            }
            for entity in self.entities
        ]

        with open(self.filename, "w") as file:
            yaml.safe_dump(data_to_write, file, allow_unicode=True)
