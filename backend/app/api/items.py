from flask_restful import Resource
import mysql.connector

class Items(Resource):
    def __init__(self, **kwargs):
        self.db = kwargs['db']

    def get(self):
        try:
            connection = self.db.get_connection()
            with connection.cursor(dictionary=True) as cursor:
                cursor.execute("SELECT id, name, description, price FROM items")
                items = cursor.fetchall()
                return items
        except Exception as e:
            return {"error": "unknown"}, 500
