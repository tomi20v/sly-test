import os

from flask import Flask
from flask_restful import Api

from app.api.items import Items

app = Flask(__name__)
api = Api(app)

@app.route("/")
def hello_world():
  """Example Hello World route."""
  name = os.environ.get("NAME", "World")
  return f"Hello {name}!"

api.add_resource(Items, '/api/items')

if __name__ == "__main__":
  app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 3000)))
