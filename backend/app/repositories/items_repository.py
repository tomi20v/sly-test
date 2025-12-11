import mysql.connector
from app.helpers import to_json_serializable

class ItemsRepository:
    def __init__(self, db):
        self.db = db

    def get_all(self):
        try:
            connection = self.db.get_connection()
            with connection.cursor(dictionary=True) as cursor:
                cursor.execute("SELECT id, name, description, price FROM items")
                items = cursor.fetchall()
                return to_json_serializable(items)
        except mysql.connector.Error as e:
            raise e

    def exists(self, item_id: int) -> bool:
        try:
            connection = self.db.get_connection()
            with connection.cursor() as cursor:
                cursor.execute("SELECT 1 FROM items WHERE id = %s", (item_id,))
                return cursor.fetchone() is not None
        except mysql.connector.Error as e:
            raise e
