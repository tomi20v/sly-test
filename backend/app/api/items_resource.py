from flask_restful import Resource

class ItemsResource(Resource):
  def __init__(self, **kwargs):
      self.items_repository = kwargs['items_repository']

  def get(self):
      try:
          items = self.items_repository.get_all()
          return items, 200
      except Exception as e:
          return {"error": "unknown", "details": str(e)}, 500