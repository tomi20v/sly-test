import json

class WebhookLogsRepository:
    def __init__(self, db):
        self._db = db

    def create(self, data):
        conn = self._db.get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO webhook_logs (data) VALUES (%s)",
            (json.dumps(data),)
        )
        conn.commit()
        new_id = cursor.lastrowid
        cursor.close()
        return new_id
