
from mysql.connector.connection import MySQLConnection

class PurchasesRepository:
    def __init__(self, db: MySQLConnection):
        self.db = db

    def create(self, user_id: int, item_id: int, price: float, xsolla_token: str) -> dict:
        connection = self.db.get_connection()
        with connection.cursor(dictionary=True) as cursor:
            cursor.execute(
                "INSERT INTO purchases (user_id, item_id, price, created_at, xsolla_token) VALUES (%s, %s, %s, NOW(), %s)",
                (user_id, item_id, price, xsolla_token)
            )
            purchase_id = cursor.lastrowid
            connection.commit()
        
        return self.get(purchase_id)

    def get(self, purchase_id: int) -> dict:
        connection = self.db.get_connection()
        with connection.cursor(dictionary=True) as cursor:
            cursor.execute("SELECT * FROM purchases WHERE id = %s", (purchase_id,))
            purchase = cursor.fetchone()
            return purchase
