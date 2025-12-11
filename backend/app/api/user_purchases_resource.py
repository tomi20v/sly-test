
from flask_restful import Resource
from app.helpers import to_json_serializable_array

class UserPurchasesResource(Resource):
    def __init__(self, purchases_repository):
        self.purchases_repository = purchases_repository

    def get(self, user_id):
        purchases = self.purchases_repository.get_users_purchases(user_id)
        return to_json_serializable_array(purchases)
