import mysql.connector

class Database:
    def __init__(self, host, user, password, database):
        self._connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )

    def get_connection(self):
        if not self._connection.is_connected():
            self._connection.reconnect()
        return self._connection

    def close(self):
        if self._connection and self._connection.is_connected():
            self._connection.close()
