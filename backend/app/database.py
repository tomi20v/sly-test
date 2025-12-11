import mysql.connector
from mysql.connector import pooling

class Database:
    def __init__(self, host, user, password, database):
        self._pool = mysql.connector.pooling.MySQLConnectionPool(
            pool_name="mypool",
            pool_size=5,
            host=host,
            user=user,
            password=password,
            database=database
        )

    def get_connection(self):
        return self._pool.get_connection()

    def close(self):
        pass
