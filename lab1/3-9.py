class Client:
    def __init__(self, client_id, surname, first_name, patronymic, comment):
        # Используем статические методы для валидации
        if not self.validate_client_id(client_id):
            raise ValueError("Invalid client ID")
        if not self.validate_text_field(surname, "surname"):
            raise ValueError("Invalid surname")
        if not self.validate_text_field(first_name, "first name"):
            raise ValueError("Invalid first name")
        if not self.validate_text_field(patronymic, "patronymic"):
            raise ValueError("Invalid patronymic")
        if not self.validate_comment(comment):
            raise ValueError("Invalid comment")

        # Присваиваем значения приватным атрибутам
        self.__client_id = client_id
        self.__surname = surname
        self.__first_name = first_name
        self.__patronymic = patronymic
        self.__comment = comment

    # Геттер и сеттер для client_id
    def get_client_id(self):
        return self.__client_id

    def set_client_id(self, client_id):
        if not self.validate_client_id(client_id):
            raise ValueError("Invalid client ID")
        self.__client_id = client_id

    # Геттер и сеттер для surname
    def get_surname(self):
        return self.__surname

    def set_surname(self, surname):
        if not self.validate_surname(surname):
            raise ValueError("Invalid surname")
        self.__surname = surname

    # Геттер и сеттер для first_name
    def get_first_name(self):
        return self.__first_name

    def set_first_name(self, first_name):
        if not self.validate_first_name(first_name):
            raise ValueError("Invalid first name")
        self.__first_name = first_name

    # Геттер и сеттер для patronymic
    def get_patronymic(self):
        return self.__patronymic

    def set_patronymic(self, patronymic):
        if not self.validate_patronymic(patronymic):
            raise ValueError("Invalid patronymic")
        self.__patronymic = patronymic

    # Геттер и сеттер для comment
    def get_comment(self):
        return self.__comment

    def set_comment(self, comment):
        if not self.validate_comment(comment):
            raise ValueError("Invalid comment")
        self.__comment = comment


    # Статические методы для валидации
    @staticmethod
    def validate_client_id(client_id):
        return isinstance(client_id, int) and client_id > 0

    @staticmethod
    def validate_text_field(field, field_name):
        return isinstance(field, str) and bool(field.strip())

    @staticmethod
    def validate_comment(comment):
        # допустим, комментарий – это необязательное поле
        return isinstance(comment, str)