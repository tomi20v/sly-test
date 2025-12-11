import mysql.connector
from app.helpers import to_json_serializable, to_json_serializable_array

class ItemNotFoundError(Exception):
    pass

class ItemsRepository:
    def __init__(self, db):
        self.db = db

    def get_all(self):
        try:
            connection = self.db.get_connection()
            with connection.cursor(dictionary=True) as cursor:
                cursor.execute("SELECT id, name, description, price FROM items")
                items = cursor.fetchall()
                return to_json_serializable_array(items)
        except mysql.connector.Error as e:
            raise e

    def get(self, item_id: int):
        try:
            connection = self.db.get_connection()
            with connection.cursor(dictionary=True) as cursor:
                cursor.execute("SELECT id, name, description, price FROM items WHERE id = %s", (item_id,))
                item = cursor.fetchone()
                if not item:
                    raise ItemNotFoundError(f"Item with id {item_id} not found")
                return to_json_serializable(item)
        except mysql.connector.Error as e:
            raise e
