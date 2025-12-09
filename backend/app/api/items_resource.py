from flask_restful import Resource
import mysql.connector
import time
from app.helpers import to_json_serializable

class ItemsResource(Resource):
    def __init__(self, **kwargs):
        self.db = kwargs['db']

    def get(self):
        try:
            connection = self.db.get_connection()
            with connection.cursor(dictionary=True) as cursor:
                cursor.execute("SELECT id, name, description, price FROM items")
                items = cursor.fetchall()
                return to_json_serializable(items)
        except Exception as e:
            return {"error": "unknown"}, 500
