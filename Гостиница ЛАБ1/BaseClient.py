import json
import re
class ClientValidator:
    field_validators = {
        'client_id': lambda cls, value: value is None or cls.validate_client_id(value),
        'surname': lambda cls, value: cls.validate_text_field_no_digits(value, 'surname'),
        'first_name': lambda cls, value: cls.validate_text_field_no_digits(value, 'first_name'),
        'patronymic': lambda cls, value: cls.validate_text_field_no_digits(value, 'patronymic'),
        'email': lambda cls, value: cls.validate_email(value),
        'phone_number': lambda cls, value: cls.validate_phone_number(value),
        'passport_number': lambda cls, value: cls.validate_passport_number(value),
        'comment': lambda cls, value: cls.validate_text_field_no_digits(value, 'comment')
    }

    def validate_attr(cls, name, value):
        """Проверяет значение атрибута по правилам в field_validators."""
        if name in cls.field_validators:
            return cls.field_validators[name](cls, value)
        return True  # Если атрибут не указан в валидаторе, считать его корректным

    @staticmethod
    def validate_client_id(client_id):
        return isinstance(client_id, int) and client_id > 0

    @staticmethod
    def validate_text_field_no_digits(field, field_name):
        return isinstance(field, str) and bool(field.strip()) and not any(char.isdigit() for char in field)

    @staticmethod
    def validate_email(email):
        # Простая валидация email с использованием регулярного выражения
        pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
        return isinstance(email, str) and re.match(pattern, email) is not None

    @staticmethod
    def validate_phone_number(phone_number):
        # Проверка, что номер телефона состоит только из цифр и, возможно, начинается с +
        pattern = r"^\+?\d+$"
        return isinstance(phone_number, str) and re.match(pattern, phone_number) is not None

    @staticmethod
    def validate_passport_number(passport_number):
        return isinstance(passport_number, str)


class BaseClient:
    def __init__(self, client_id=None, surname="", first_name=""):
        self._validator = ClientValidator()
        self.client_id = client_id
        self.surname = surname
        self.first_name = first_name

    def __setattr__(self, name, value):
        if name.startswith('_'):
            return super().__setattr__(name, value)
        if self._validator.validate_attr(name, value):
            return super().__setattr__(name, value)
        else:
            raise ValueError(f"Некорректное значение для поля '{name}'")

    def __getParsedDataFromString(self, string):
        parsed_data = {}
        pairs = string.split(',')  # Используем 'string', переданное в функцию
        for pair in pairs:
            try:
                key, value = pair.split('=')
                parsed_data[key.strip()] = value.strip()
            except ValueError:
                print(f"Неправильный формат для пары: '{pair}'")  # Обработка ошибки
        return parsed_data

    @staticmethod
    def __getParsedDataFromJSON(input_json):
        try:
            return json.loads(input_json)
        except json.JSONDecodeError:
            raise ValueError("Некорректный JSON.")

    @classmethod
    def createFromJSON(cls, input_json):
        parsed_data = cls.__getParsedDataFromJSON(input_json)
        return cls(
            int(parsed_data.get('client_id', 0)),
            parsed_data.get('surname', ''),
            parsed_data.get('first_name', '')
        )

    def __eq__(self, other):
        if not isinstance(other, BaseClient):
            return NotImplemented
        return (self.surname == other.surname and
                self.first_name == other.first_name)

    def display(self):
        client_id_display = f"Client ID: {self.client_id}" if self.client_id else "Client ID: None"
        initials = f"{self.first_name[0]}." if self.first_name else ""
        return f"{client_id_display}, Surname: {self.surname}, Initials: {initials}"


class FullClient(BaseClient):
    def __init__(self, client_id=None, surname="", first_name="", patronymic="", email="", phone_number="",
                 passport_number="", comment=""):
        super().__init__(client_id, surname, first_name)
        self.patronymic = patronymic
        self.email = email
        self.phone_number = phone_number
        self.passport_number = passport_number
        self.comment = comment

    @classmethod
    def createFromString(cls, input_str):
        parsed_data = cls.__getParsedDataFromString(input_str)
        return cls(
            int(parsed_data.get('client_id', None)),
            parsed_data.get('surname', ""),
            parsed_data.get('first_name', ""),
            parsed_data.get('patronymic', ""),
            parsed_data.get('email', ""),
            parsed_data.get('phone_number', ""),
            parsed_data.get('passport_number', ""),
            parsed_data.get('comment', ""),
        )

    @classmethod
    def createFromJSON(cls, input_json):
        parsed_data = cls.__getParsedDataFromJSON(input_json)
        return cls(
            int(parsed_data.get('client_id', None)),
            parsed_data.get('surname', ""),
            parsed_data.get('first_name', ""),
            parsed_data.get('patronymic', ""),
            parsed_data.get('email', ""),
            parsed_data.get('phone_number', ""),
            parsed_data.get('passport_number', ""),
            parsed_data.get('comment', ""),
        )

    def display(self):
        client_id_display = f"Client ID: {self.client_id}" if self.client_id else "Client ID: None"
        return (f"{client_id_display}, Surname: {self.surname}, First Name: {self.first_name}, "
                f"Patronymic: {self.patronymic}, Email: {self.email}, Phone: {self.phone_number}, "
                f"Passport: {self.passport_number}, Comment: {self.comment}")

    def __eq__(self, other):
        if isinstance(other, FullClient):
            return (
                self.surname == other.surname and
                self.first_name == other.first_name and
                self.patronymic == other.patronymic and
                self.email == other.email and
                self.phone_number == other.phone_number and
                self.passport_number == other.passport_number
            )
        return super().__eq__(other)


try:
    # Создаем экземпляр FullClient с корректными данными
    full_client = FullClient(surname="Ivanov", first_name="Ivan", patronymic="Petrovich",
                             email="ivanov@example.com", phone_number="+1234567890",
                             passport_number="11212121", comment="Valid comment")
    print(full_client.display())
except ValueError as e:
    print(f"Ошибка валидации: {e}")