import pymysql
from decimal import Decimal
from Product import Product
from DBconnection import DBConnection


class ClientRepDB:
    def __init__(self, db_connection):
        """Инициализация класса с подключением к базе данных"""
        self.db_connection = db_connection  # передаем объект подключения
        self.data = self._load_data()  # загружаем все данные из базы при инициализации

    def _load_data(self):
        """Загружает все данные из базы данных (чтение всех значений)"""
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
        """Обновляет все данные в базе данных (запись всех значений)"""
        pass  # Этот метод можно использовать для обновлений, если нужно

    def read_all(self):
        """Чтение всех значений из базы"""
        return self.data

    def write_all(self):
        """Запись всех значений в базу"""
        self._save_data()

    def get_by_id(self, client_id):
        """Получить объект по ID"""
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
        """Получить список k по счету n объектов"""
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
        """Сортировка элементов по выбранному полю"""
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
        """Добавить объект в базу данных"""
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
        """Заменить элемент по ID"""
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
        """Удалить объект по ID"""
        with self.db_connection.cursor() as cursor:
            sql = "DELETE FROM my_entity WHERE client_id = %s"
            cursor.execute(sql, (client_id,))
            self.db_connection.commit()
            return cursor.rowcount > 0

    def get_count(self):
        """Получить количество объектов в базе"""
        with self.db_connection.cursor() as cursor:
            sql = "SELECT COUNT(*) AS count FROM my_entity"
            cursor.execute(sql)
            result = cursor.fetchone()
            return result['count'] if result else 0

    def close(self):
        """Закрытие соединения с базой данных"""
        self.db_connection.close()