import os
import time
from flask import Flask
from flask_restful import Api
import mysql.connector

from app.api.items_resource import ItemsResource
from app.api.purchases_resource import PurchasesResource
from app.database import Database
from app.config import Config
from app.repositories.user_repository import UserRepository
from app.repositories.items_repository import ItemsRepository

app = Flask(__name__)
api = Api(app)

try:
  # Database configuration
  config = Config()

  # Create a database instance
  db = Database(host=config.MYSQL_HOST, user=config.MYSQL_USER, password=config.MYSQL_PASSWORD, database=config.MYSQL_DATABASE)
  user_repository = UserRepository(db)
  items_repository = ItemsRepository(db)

  @app.route("/")
  def hello_world():
    """Example Hello World route."""
    name = os.environ.get("NAME", "World")
    return f"Hello {name}!"

  # Inject the database instance into the resources
  api.add_resource(ItemsResource, '/api/items', resource_class_kwargs={'items_repository': items_repository})
  api.add_resource(
      PurchasesResource, '/api/purchases', 
      resource_class_kwargs={'db': db, 'user_repository': user_repository, 'items_repository': items_repository}
  )

  @app.before_request
  def before_request():
    time.sleep(1)

  # Register a function to close the database connection when the app exits
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
