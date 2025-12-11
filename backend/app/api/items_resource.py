from flask_restful import Resource
from app.helpers import to_json_serializable, to_json_serializable_array

class ItemsResource(Resource):
  def __init__(self, **kwargs):
      self.items_repository = kwargs['items_repository']

  def get(self):
      try:
          items = self.items_repository.get_all()
          return to_json_serializable_array(items), 200
      except Exception as e:
          # NOTE: It's good practice to log the error e for debugging
          return {"error": "An unexpected error occurred"}, 500