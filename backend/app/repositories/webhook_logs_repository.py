import json

class WebhookLogsRepository:
    def __init__(self, db):
        self._db = db

    def create(self, data):
        with self._db.get_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    "INSERT INTO webhook_logs (data) VALUES (%s)",
                    (json.dumps(data),)
                )
                conn.commit()
                new_id = cursor.lastrowid
                return new_id
    
    def update(self, log_id, result, error=None):
        with self._db.get_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    "UPDATE webhook_logs SET result = %s, error = %s WHERE id = %s",
                    (result, error, log_id)
                )
                conn.commit()
