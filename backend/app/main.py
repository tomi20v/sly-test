import os
from flask import Flask
from flask_restful import Api

from app.api.items import Items
from app.database import Database
from app.config import Config

app = Flask(__name__)
api = Api(app)

try:
  # Database configuration
  config = Config()

  # Create a database instance
  db = Database(host=config.MYSQL_HOST, user=config.MYSQL_USER, password=config.MYSQL_PASSWORD, database=config.MYSQL_DATABASE)

  @app.route("/")
  def hello_world():
    """Example Hello World route."""
    name = os.environ.get("NAME", "World")
    return f"Hello {name}!"

  # Inject the database instance into the Items resource
  api.add_resource(Items, '/api/items', resource_class_kwargs={'db': db})

  # Register a function to close the database connection when the app exits 
  # (I'd have to check if it's really a good practice like this?)
  @app.teardown_appcontext
  def teardown_db(exception=None):
      if db:
          db.close()

except mysql.connector.Error as e:
  print("Database connection failed.")
  exit(1)
except Exception as e:
  print(e)
  exit(1)

if __name__ == "__main__":
  app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 3000)))
