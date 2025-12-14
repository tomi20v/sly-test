import hashlib
import time
from flask import request
from flask_restful import Resource
import mysql.connector
from app.repositories.items_repository import ItemNotFoundError
from app.helpers import to_json_serializable
from app.repositories.purchases_repository import PurchasesRepository

class PurchasesResource(Resource):
    def __init__(self, **kwargs):
        self.db = kwargs['db']
        self.users_repository = kwargs['users_repository']
        self.items_repository = kwargs['items_repository']
        self.purchases_repository = kwargs['purchases_repository']

    def get(self, purchase_id):
        try:
            purchase = self.purchases_repository.get(purchase_id)
            if purchase:
                return to_json_serializable(purchase), 200
            else:
                return {"error": "Purchase not found"}, 404
        except mysql.connector.Error as e:
            # NOTE: It's good practice to log the error e for debugging
            return {"error": "Database error"}, 500
        except Exception as e:
            # NOTE: It's good practice to log the error e for debugging
            return {"error": "An unexpected error occurred"}, 500
    
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
            user_id = self.users_repository.get_or_create_by_email(email)
                
            # 4. Generate Xsolla token
            xsolla_token = hashlib.sha256(f"{email}{item_id}{time.time()}".encode()).hexdigest()

            # 5. Create purchase in DB
            new_purchase = self.purchases_repository.create(user_id, item_id, item['price'], xsolla_token)

            return to_json_serializable(new_purchase), 200
        except ItemNotFoundError as e:
            return {"item_id": "item_id does not exist"}, 400
        except mysql.connector.Error as e:
            # NOTE: It's good practice to log the error e for debugging
            return {"error": "Database error"}, 500
        except Exception as e:
            # NOTE: It's good practice to log the error e for debugging
            return {"error": "An unexpected error occurred"}, 500
