import pymysql

class DBConnection:
    _instance = None  # Статическая переменная для хранения единственного экземпляра

    def __new__(cls, host='localhost', user='root', password='', db='my_database'):
        if not cls._instance:
            cls._instance = super().__new__(cls)
            cls._instance._connect(host, user, password, db)
        return cls._instance

    def _connect(self, host, user, password, db):
        self.connection = pymysql.connect(
            host=host,
            user=user,
            password=password,
            database=db,
            cursorclass=pymysql.cursors.DictCursor  # Возвращать строки как словари
        )

    def get_connection(self):
        return self.connection

    def close(self):
        if self.connection:
            self.connection.close()
