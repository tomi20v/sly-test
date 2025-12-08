from flask_restful import Resource

class Items(Resource):
    def get(self):
        return [{"id": 1, "name": "Cool Skin", "price": 100}]
