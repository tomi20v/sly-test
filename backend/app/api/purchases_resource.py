import hashlib
import time
from flask import request
from flask_restful import Resource
import mysql.connector
from app.repositories.items_repository import ItemNotFoundError

class PurchasesResource(Resource):
    def __init__(self, **kwargs):
        self.db = kwargs['db']
        self.user_repository = kwargs['user_repository']
        self.items_repository = kwargs['items_repository']

    def post(self):
        # 1. Validate input
        data = request.get_json()
        if not data:
            return {"error": "Invalid JSON"}, 400

        if 'email' not in data:
            return {'email': 'email is required'}, 400

        if 'item_id' not in data:
            return {'item_id': 'item_id is required'}, 400

        email = data['email']
        item_id = data['item_id']

        if not isinstance(item_id, int):
            return {'item_id': 'item_id must be an integer'}, 400

        try:
            # 2. Check if item exists and get price
            item = self.items_repository.get(item_id)

            # 3. Get or create user
            user_id = self.user_repository.get_or_create_by_email(email)
                
            # 4. Generate Xsolla token
            xsolla_token = hashlib.sha256(f"{email}{item_id}{time.time()}".encode()).hexdigest()

            connection = self.db.get_connection()
            with connection.cursor(dictionary=True) as cursor:
              # 5. Create purchase in DB
              cursor.execute(
                  "INSERT INTO purchases (user_id, item_id, price, created_at, xsolla_token) VALUES (%s, %s, %s, NOW(), %s)",
                  (user_id, item_id, item['price'], xsolla_token)
              )
              connection.commit()

            return {"xsolla_token": xsolla_token}, 200
        except ItemNotFoundError as e:
            return {"item_id": "item_id does not exist"}, 400
        except mysql.connector.Error as e:
            # NOTE: It's good practice to log the error e for debugging
            return {"error": "Database error"}, 500
        except Exception as e:
            # NOTE: It's good practice to log the error e for debugging
            return {"error": "An unexpected error occurred"}, 500
