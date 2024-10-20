import json

class BaseClient:
    def __init__(self, client_id, surname="", first_name="", patronymic="", comment=""):

        # **Добавлено для поддержки строкового или JSON ввода**
        if isinstance(client_id, str):
            parsed_data = self.parse_input(client_id)
            self.client_id = int(parsed_data.get('client_id', 0))
            self.surname = parsed_data.get('surname', "")
            self.first_name = parsed_data.get('first_name', "")
            self.patronymic = parsed_data.get('patronymic', "")
            self.comment = parsed_data.get('comment', "")

        else:
            self.client_id = client_id
            self.surname = surname
            self.first_name = first_name
            self.patronymic = patronymic
            self.comment = comment      

       
    def parse_input(self, input_data):
        try:
            return json.loads(input_data)
        except json.JSONDecodeError:
            parsed_data = {}
            pairs = input_data.split(',')
            for pair in pairs:
                key, value = pair.split('=')
                parsed_data[key.strip()] = value.strip()
            return parsed_data      
    @staticmethod
    def validate_client_id(client_id):
        return isinstance(client_id, int) and client_id > 0

    @staticmethod
    def validate_text_field(field, field_name):
        return isinstance(field, str) and bool(field.strip())

    @staticmethod
    def validate_comment(comment):
        return isinstance(comment, str)
    
class FullClient(BaseClient):
    def __init__(self, client_id, surname="", first_name="", patronymic="", comment=""):
        super().__init__(client_id, surname, first_name, patronymic, comment)
        
        if not self.validate_client_id(self.client_id):
            raise ValueError("Invalid client ID")
        if not self.validate_text_field(self.surname, "surname"):
            raise ValueError("Invalid surname")
        if not self.validate_text_field(self.first_name, "first name"):
            raise ValueError("Invalid first name")
        if not self.validate_text_field(self.patronymic, "patronymic"):
            raise ValueError("Invalid patronymic")
        if not self.validate_comment(self.comment):
            raise ValueError("Invalid comment")
    def display_full_version(self):
        return f"Client ID: {self.client_id}, Surname: {self.surname}, First Name: {self.first_name}, Patronymic: {self.patronymic}, Comment: {self.comment}"
    
class ClientSummary(BaseClient):
    def __init__(self, client_id, surname="", first_name=""):
        super().__init__(client_id, surname, first_name)

    def display_summary(self):
        return f"Client ID: {self.client_id}, Surname: {self.surname}, First Name: {self.first_name}"

full_client = FullClient(client_id="client_id=1,surname=Ivanov,first_name=Ivan,patronymic=Petrovich,comment=Important client")
print(full_client.display_full_version())

client_summary = ClientSummary(client_id="client_id=1,surname=Ivanov,first_name=Ivan")
print(client_summary.display_summary())