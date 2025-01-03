import json
import yaml

from BaseClient import FullClient
from ClientStrategy import ClientStrategy
from Client_rep_json import ClientRepJson
from Client_rep_yaml import ClientRepYaml

class ClientRepBase:
    def __init__(self, filename, strategy: ClientStrategy):
        self.filename = filename
        self.strategy = strategy
        self.clients = self._read_from_file()

    def _read_from_file(self):
        if isinstance(self.strategy, ClientRepJson):
            return self.strategy._read_from_file()
        elif isinstance(self.strategy, ClientRepYaml):
            return self.strategy._read_from_file()
        return []

    def _write_to_file(self):
        if isinstance(self.strategy, ClientRepJson):
            self.strategy._write_to_file()
        elif isinstance(self.strategy, ClientRepYaml):
            self.strategy._write_to_file()

    def get_all(self):
        return self.clients

    def get_by_id(self, client_id):
        for client in self.clients:
            if client.client_id == client_id:
                return client
        return None

    def get_k_n_short_list(self, n, k):
        start_index = n * (k - 1)
        end_index = start_index + n
        return self.clients[start_index:end_index]

    def sort_by_field(self, field_name):
        def get_field_value(client):
            if hasattr(client, field_name):
                return getattr(client, field_name)
            return None

        self.clients.sort(key=get_field_value)
        self._write_to_file()

    def is_client_exist_by_passport(self, passport_number):
        for client in self.clients:
            if client.passport_number == passport_number:
                return True
        return False

    def add_client(self, surname, first_name, patronymic, email, phone_number, passport_number, comment):
        if self.is_client_exist_by_passport(passport_number):
            raise ValueError(f"Клиент с паспортным номером {passport_number} уже существует")

        max_id = 0
        for client in self.clients:
            if client.client_id is not None and client.client_id > max_id:
                max_id = client.client_id
        new_id = max_id + 1

        new_client = FullClient(new_id, surname, first_name, patronymic, email, phone_number, passport_number, comment)
        self.clients.append(new_client)
        self.strategy.clients = self.clients
        self._write_to_file()

    def update_client_by_id(self, client_id, **kwargs):
        client = self.get_by_id(client_id)
        if client is not None:
            for key, value in kwargs.items():
                if hasattr(client, key):
                    setattr(client, key, value)
            self._write_to_file()
        else:
            raise ValueError(f"Клиент с ID {client_id} не найден")

    def delete_client_by_id(self, client_id):
        updated_clients = []
        for client in self.clients:
            if client.client_id != client_id:
                updated_clients.append(client)
        self.clients = updated_clients
        self._write_to_file()

    def get_count(self):
        return len(self.clients)

    @staticmethod
    def convert_data(input_filename, output_filename, input_strategy_class, output_strategy_class):
        input_repository = input_strategy_class(input_filename)
        clients = input_repository.clients

        output_repository = output_strategy_class(output_filename)
        output_repository.clients = clients
        output_repository._write_to_file()

        print(f"Данные успешно сконвертированы из {input_filename} в {output_filename}.")


if __name__ == "__main__":
    input_json_file = "test.json"
    output_yaml_file = "output.yaml"
    # Экземпляры JSON и YAML репозиториев
    json_repository = ClientRepJson(input_json_file)
    yaml_repository = ClientRepYaml(output_yaml_file)

    # Создаем объект ClientRepBase для работы с JSON
    json_base = ClientRepBase(input_json_file, json_repository)

    json_base.add_client(
        surname="Иванов",
        first_name="Иван",
        patronymic="Иванович",
        email="ivanov@example.com",
        phone_number="1234567890",
        passport_number="123456789",
        comment="Пример клиента"
    )
    json_base.add_client(
        surname="Петров",
        first_name="Петр",
        patronymic="Петрович",
        email="petrov@example.com",
        phone_number="0987654321",
        passport_number="987654321",
        comment="Второй клиент"
    )


    for client in json_base.get_all():
        print(f"Client ID: {client.client_id}, Surname: {client.surname}, First Name: {client.first_name}")

    print("\nСортировка по фамилии:")
    json_base.sort_by_field("surname")
    for client in json_base.get_all():
        print(f"Client ID: {client.client_id}, Surname: {client.surname}")

    print("\nУдаление клиента с ID 1:")
    json_base.delete_client_by_id(1)
    for client in json_base.get_all():
        print(f"Client ID: {client.client_id}, Surname: {client.surname}")

    print("\nОбновление клиента с ID 2:")
    json_base.update_client_by_id(2, phone_number="5555555555")
    print(json_base.get_by_id(2))

    print("\nСписок клиентов (2 первых записи):")
    short_list = json_base.get_k_n_short_list(2, 1)
    for client in short_list:
        print(f"Client ID: {client.client_id}, Surname: {client.surname}")


    print(f"\nКоличество клиентов: {json_base.get_count()}")


    print(json_base.is_client_exist_by_passport("123456789"))

    ClientRepBase.convert_data(input_json_file, output_yaml_file, ClientRepJson, ClientRepYaml)





