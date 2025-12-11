import os
import time
from flask import Flask
from flask_restful import Api
import mysql.connector

from app.api.items_resource import ItemsResource
from app.api.purchases_resource import PurchasesResource
from app.api.user_purchases_resource import UserPurchasesResource
from app.api.webhooks_resource import WebhooksResource
from app.database import Database
from app.config import Config
from app.repositories.user_repository import UserRepository
from app.repositories.items_repository import ItemsRepository
from app.repositories.purchases_repository import PurchasesRepository
from app.repositories.webhook_logs_repository import WebhookLogsRepository

app = Flask(__name__)
api = Api(app)

try:
  # Database configuration
  config = Config()

  # Create a database instance
  db = Database(host=config.MYSQL_HOST, user=config.MYSQL_USER, password=config.MYSQL_PASSWORD, database=config.MYSQL_DATABASE)
  user_repository = UserRepository(db)
  items_repository = ItemsRepository(db)
  purchases_repository = PurchasesRepository(db)
  webhook_logs_repository = WebhookLogsRepository(db)

  @app.route("/")
  def hello_world():
    """Example Hello World route."""
    name = os.environ.get("NAME", "World")
    return f"Hello {name}!"

  # Inject the database instance into the resources
  api.add_resource(ItemsResource, '/api/items', resource_class_kwargs={'items_repository': items_repository})
  api.add_resource(
      PurchasesResource, 
      '/api/purchases', 
      '/api/purchases/<int:purchase_id>',
      resource_class_kwargs={'db': db, 'user_repository': user_repository, 'items_repository': items_repository, 'purchases_repository': purchases_repository}
  )
  api.add_resource(UserPurchasesResource, '/api/users/<int:user_id>/purchases', resource_class_kwargs={'purchases_repository': purchases_repository})
  api.add_resource(WebhooksResource, '/api/webhooks/payment', resource_class_kwargs={'purchases_repository': purchases_repository, 'webhook_logs_repository': webhook_logs_repository})


  # this serves simulating slow load and errors in the backend for development
  # @todo remove it or make it depend on an env var (errors could be 50% random)
  @app.before_request
  def before_request():
    time.sleep(1)
    #return "Internal Server Error", 500

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
