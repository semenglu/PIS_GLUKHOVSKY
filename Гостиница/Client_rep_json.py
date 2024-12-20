import json


class ClientRepJson(ClientRepBase):
    def __init__(self, filename):
        self.filename = filename
        self.clients = self._read_from_file()

    def _read_from_file(self):
        try:
            with open(self.filename, "r") as file:
                data = json.load(file)
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
        except json.JSONDecodeError:
            return []

    def _write_to_file(self):
        data_to_write = []
        for client in self.clients:
            client_data = {
                "client_id": client.client_id,
                "surname": client.surname,
                "first_name": client.first_name,
                "patronymic": client.patronymic,
                "email": client.email,
                "phone_number": client.phone_number,
                "passport_number": client.passport_number,
                "comment": client.comment,
            }
            data_to_write.append(client_data)

        with open(self.filename, "w") as file:
            json.dump(data_to_write, file)

