import json
from BaseClient import FullClient
from ClientStrategy import ClientStrategy

class ClientRepJson(ClientStrategy):
    def __init__(self, filename):
        self.filename = filename
        self.clients = self._read_from_file()

    def _read_from_file(self):
        try:
            with open(self.filename, "r", encoding="utf-8") as file:
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
            with open(self.filename, "w", encoding="utf-8") as file:
                json.dump([], file, ensure_ascii=False, indent=4)
            return []
        except json.JSONDecodeError:
            with open(self.filename, "w", encoding="utf-8") as file:
                json.dump([], file, ensure_ascii=False, indent=4)
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

        with open(self.filename, "w", encoding="utf-8") as file:
            json.dump(data_to_write, file, ensure_ascii=False, indent=4)

            # Логируем, что собираемся записать
        print("Запись данных в файл:")
        print(data_to_write)

        # Логируем успешную запись
        print(f"Данные успешно записаны в {self.filename}")