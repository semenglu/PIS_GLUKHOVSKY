import pymysql
from decimal import Decimal
from Product import Product
from DBconnection import DBConnection


class ClientRepDB:
    def __init__(self, host, user, password, database, port=3306):
        self.db_connection = DBConnection(host, user, password, database, port)

    def _load_data(self):
        with self.db_connection.cursor(pymysql.cursors.DictCursor) as cursor:
            sql = "SELECT * FROM my_entity"  # замените 'my_entity' на название вашей таблицы
            cursor.execute(sql)
            result = cursor.fetchall()
            return [
                MyEntity(
                    client_id=row['client_id'],
                    surname=row['surname'],
                    first_name=row['first_name'],
                    patronymic=row['patronymic'],
                    email=row['email'],
                    phone_number=row['phone_number'],
                    passport_number=row['passport_number'],
                    comment=row['comment']
                ) for row in result
            ]

    def _save_data(self):
        pass  # Этот метод можно использовать для обновлений, если нужно

    def read_all(self):
        return self.data

    def write_all(self):
        self._save_data()

    def get_by_id(self, client_id):
        with self.db_connection.cursor(pymysql.cursors.DictCursor) as cursor:
            sql = "SELECT * FROM my_entity WHERE client_id = %s"  # Замените на вашу таблицу
            cursor.execute(sql, (client_id,))
            result = cursor.fetchone()
            if result:
                return MyEntity(
                    client_id=result['client_id'],
                    surname=result['surname'],
                    first_name=result['first_name'],
                    patronymic=result['patronymic'],
                    email=result['email'],
                    phone_number=result['phone_number'],
                    passport_number=result['passport_number'],
                    comment=result['comment']
                )
            return None

    def get_k_n_short_list(self, k, n):
        offset = (n - 1) * k
        with self.db_connection.cursor(pymysql.cursors.DictCursor) as cursor:
            sql = "SELECT * FROM my_entity LIMIT %s OFFSET %s"  # Пагинация
            cursor.execute(sql, (k, offset))
            result = cursor.fetchall()
            return [
                MyEntity(
                    client_id=row['client_id'],
                    surname=row['surname'],
                    first_name=row['first_name'],
                    patronymic=row['patronymic'],
                    email=row['email'],
                    phone_number=row['phone_number'],
                    passport_number=row['passport_number'],
                    comment=row['comment']
                ) for row in result
            ]

    def sort_by_field(self, field_name, ascending=True):
        with self.db_connection.cursor(pymysql.cursors.DictCursor) as cursor:
            sql = f"SELECT * FROM my_entity ORDER BY {field_name} {'ASC' if ascending else 'DESC'}"
            cursor.execute(sql)
            result = cursor.fetchall()
            return [
                MyEntity(
                    client_id=row['client_id'],
                    surname=row['surname'],
                    first_name=row['first_name'],
                    patronymic=row['patronymic'],
                    email=row['email'],
                    phone_number=row['phone_number'],
                    passport_number=row['passport_number'],
                    comment=row['comment']
                ) for row in result
            ]

    def add_entity(self, entity):
        entity.client_id = uuid.uuid4().int  # Генерация уникального ID
        with self.db_connection.cursor() as cursor:
            sql = """
                INSERT INTO my_entity (surname, first_name, patronymic, email, phone_number, passport_number, comment)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
            """
            cursor.execute(sql, (
                entity.surname,
                entity.first_name,
                entity.patronymic,
                entity.email,
                entity.phone_number,
                entity.passport_number,
                entity.comment
            ))
            self.db_connection.commit()
            entity.client_id = cursor.lastrowid  # Получаем ID, сгенерированный базой
            return entity.client_id

    def replace_entity(self, client_id, new_entity):
        with self.db_connection.cursor() as cursor:
            sql = """
                UPDATE my_entity
                SET surname = %s, first_name = %s, patronymic = %s, email = %s, 
                    phone_number = %s, passport_number = %s, comment = %s
                WHERE client_id = %s
            """
            cursor.execute(sql, (
                new_entity.surname,
                new_entity.first_name,
                new_entity.patronymic,
                new_entity.email,
                new_entity.phone_number,
                new_entity.passport_number,
                new_entity.comment,
                client_id
            ))
            self.db_connection.commit()
            return cursor.rowcount > 0

    def delete_entity(self, client_id):
        with self.db_connection.cursor() as cursor:
            sql = "DELETE FROM my_entity WHERE client_id = %s"
            cursor.execute(sql, (client_id,))
            self.db_connection.commit()
            return cursor.rowcount > 0

    def get_count(self):
        with self.db_connection.cursor() as cursor:
            sql = "SELECT COUNT(*) AS count FROM my_entity"
            cursor.execute(sql)
            result = cursor.fetchone()
            return result['count'] if result else 0

    def close(self):
        self.db_connection.close()