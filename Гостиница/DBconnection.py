import pymysql
from pymysql.cursors import DictCursor


class DatabaseConnection:
    _instance = None

    def __new__(cls, host, user, password, database):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.connection = pymysql.connect(
                host=host,
                user=user,
                password=password,
                database=database,
                cursorclass=DictCursor
            )
        return cls._instance

    def get_connection(self):
        return self.connection
