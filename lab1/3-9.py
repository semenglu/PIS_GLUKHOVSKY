import json
import re



class ClientValidator:
    field_validators = {
        'client_id': self.validate_client_id,
        'surname': self.validate_text_field_no_digits,
        'first_name': self.validate_text_field_no_digits,
        'patronymic': self.validate_text_field_no_digits,
        'email': self.validate_email,
        'phone_number': self.validate_email,
        'passport_number': self.passport_number
    }

    def validate_attr(name, value):
        if value is not None:
            return self.field_validators['name'](value)
        return None

    @staticmethod
    def validate_client_id(client_id):
        if isinstance(client_id, int) and client_id > 0:
            return client_id
        else:
            raise ValueError()

    @staticmethod
    def validate_text_field_no_digits(field, field_name):
        if isinstance(field, str) and bool(field.strip()) and not any(char.isdigit() for char in field):
            return field
        else:
            raise ValueError()

    @staticmethod
    def validate_email(email):
        # Простая валидация email с использованием регулярного выражения
        pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
        if isinstance(email, str) and re.match(pattern, email) is not None:
            return email
        else:
            raise ValueError()

    @staticmethod
    def validate_phone_number(phone_number):
        # Проверка, что номер телефона состоит только из цифр и, возможно, начинается с +
        pattern = r"^\+?\d+$"
        if isinstance(phone_number, str) and re.match(pattern, phone_number) is not None:
            return phone_number
        else:
            raise ValueError()

    @staticmethod
    def validate_passport_number(passport_number):
        if isinstance(passport_number, str)
            return passport_number
        else:
            raise ValueError()

class BaseClient:
    def __init__(self, client_id, surname=None, first_name=None, patronymic=None, email=None, phone_number=None,passport_number=None, comment=None):
                
                self.__validator = ClientValidator()
                self.client_id = client_id
                self.surname = surname
                self.first_name = first_name
                self.patronymic = patronymic
                self.email = email
                self.phone_number = phone_number
                self.passport_number = passport_number
                self.comment = comment

    def __setattr__(self, name, value):
                self.name = self.__validator.validate_attr(name, value)
       
    @staticmethod
    def createFromString(self, input_str):
        parsed_data = {}
        pairs = input_str.split(',')
        for pair in pairs:
            key, value = pair.split('=')
            parsed_data[key.strip()] = value.strip()
        return self.__init__(
            int(parsed_data['client_id']),
            parsed_data['surname'],
            parsed_data['first_name'],
            parsed_data['patronymic'],
            parsed_data['email'],
            parsed_data['phone_number'],
            parsed_data['passport_number'],
            parsed_data['comment'],
        )

    @staticmethod
    def createFromJSON(self, input_json):
        parsed_data = json.loads(input_json)
        return self.__init__(
            int(parsed_data['client_id']),
            parsed_data['surname'],
            parsed_data['first_name'],
            parsed_data['patronymic'],
            parsed_data['email'],
            parsed_data['phone_number'],
            parsed_data['passport_number'],
            parsed_data['comment'],
        )

    
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