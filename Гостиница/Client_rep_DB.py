import pymysql

from DBconnection import DatabaseConnection


class ClientRepDB:
    def __init__(self, db_connection):
        self.connection = db_connection

    def get_by_id(self, client_id):
        with self.connection.cursor() as cursor:
            query = "SELECT * FROM clients WHERE id = %s"
            cursor.execute(query, (client_id,))
            result = cursor.fetchone()
            return result

    def get_k_n_short_list(self, n, k):
        with self.connection.cursor() as cursor:
            offset = n * (k - 1)
            query = "SELECT * FROM clients LIMIT %s OFFSET %s"
            cursor.execute(query, (n, offset))
            result = cursor.fetchall()
            return result

    def add_client(self, name, email, phone):
        with self.connection.cursor() as cursor:
            query = "INSERT INTO clients (name, email, phone) VALUES (%s, %s, %s)"
            cursor.execute(query, (name, email, phone))
            self.connection.commit()

    def update_client_by_id(self, client_id, name=None, email=None, phone=None):
        query = "UPDATE clients SET "
        params = []
        if name:
            query += "name = %s, "
            params.append(name)
        if email:
            query += "email = %s, "
            params.append(email)
        if phone:
            query += "phone = %s, "
            params.append(phone)

        query = query.rstrip(', ') + " WHERE id = %s"
        params.append(client_id)

        with self.connection.cursor() as cursor:
            cursor.execute(query, tuple(params))
            self.connection.commit()

    def delete_client_by_id(self, client_id):
        with self.connection.cursor() as cursor:
            query = "DELETE FROM clients WHERE id = %s"
            cursor.execute(query, (client_id,))
            self.connection.commit()

    def get_count(self):
        with self.connection.cursor() as cursor:
            query = "SELECT COUNT(*) as count FROM clients"
            cursor.execute(query)
            result = cursor.fetchone()
            return result['count']


# ▎Использование в главной функции
if __name__ == "__main__":
    # Создаем подключение к базе данных с помощью класса Singleton
    db_conn = DatabaseConnection(
        host="localhost",
        user="root",
        password="1234567890",
        database="Local instance MySQL91"
    ).get_connection()

    # Создаем экземпляр ClientRepDB, передавая подключение
    db = ClientRepDB(db_conn)

    db.add_client("Иван Иванов", "ivanovSDDDDS1@example.com", "1234567890")
    db.add_client("Пётр Петров", "petrovDDDSDSD1@example.com", "0987654321")

    client = db.get_by_id(1)
    print("Клиент с ID 1:", client)

    clients = db.get_k_n_short_list(2, 1)
    print("Список клиентов:", clients)

    db.update_client_by_id(1, name="Иван Иванович", email="ivan_updated@example.com")
    db.delete_client_by_id(2)

    count = db.get_count()
    print("Количество клиентов:", count)

