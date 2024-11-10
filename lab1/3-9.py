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

    def __eq__(self, other):
        if not isinstance(other, BaseClient):
            return NotImplemented
        return (self.client_id == other.client_id and
                self.surname == other.surname and
                self.first_name == other.first_name and
                self.patronymic == other.patronymic and
                self.email == other.email and
                self.phone_number == other.phone_number and
                self.passport_number == other.passport_number)
    
class FullClient(BaseClient):
    def __init__(self, client_id, surname="", first_name="", patronymic="",email="", phone_number="", passport_number="", comment=""):
        super().__init__(client_id, surname, first_name, patronymic, email, phone_number, passport_number, comment)
        
    def display_full_version(self):
        return (f"Client ID: {self.client_id}, Surname: {self.surname}, First Name: {self.first_name}, "
                f"Patronymic: {self.patronymic}, Email: {self.email}, Phone: {self.phone_number}, "
                f"Passport: {self.passport_number}, Comment: {self.comment}")
    
class ShortClient(BaseClient):
    def __init__(self, client_id, surname="", first_name=""):
        super().__init__(client_id, surname, first_name)

    def __eq__(self, other):
        if not isinstance(other, BaseClient):
            return NotImplemented
        return (self.client_id == other.client_id and
                self.surname == other.surname and
                self.first_name == other.first_name)

    def display_summary(self):
        initials = f"{self.first_name[0]}." if self.first_name else ""
        patronymic_initial = f"{self.patronymic[0]}." if self.patronymic else ""
        return f"Client ID: {self.client_id}, Surname: {self.surname}, Initials: {initials}{patronymic_initial}"
