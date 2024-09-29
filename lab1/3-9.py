class Client:
    def __init__(self, client_id, surname, first_name, patronymic, comment):
        self.__client_id = client_id
        self.__surname = surname
        self.__first_name = first_name
        self.__patronymic = patronymic
        self.__comment = comment

    # Геттер и сеттер для client_id
    def get_client_id(self):
        return self.__client_id

    def set_client_id(self, client_id):
        self.__client_id = client_id

    # Геттер и сеттер для surname
    def get_surname(self):
        return self.__surname

    def set_surname(self, surname):
        self.__surname = surname

    # Геттер и сеттер для first_name
    def get_first_name(self):
        return self.__first_name

    def set_first_name(self, first_name):
        self.__first_name = first_name

    # Геттер и сеттер для patronymic
    def get_patronymic(self):
        return self.__patronymic

    def set_patronymic(self, patronymic):
        self.__patronymic = patronymic

    # Геттер и сеттер для comment
    def get_comment(self):
        return self.__comment

    def set_comment(self, comment):
        self.__comment = comment