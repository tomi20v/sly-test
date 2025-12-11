import mysql.connector

class UserRepository:
    def __init__(self, db):
        self.db = db

    def get_or_create_by_email(self, email: str) -> int:
        try:
            connection = self.db.get_connection()
            with connection.cursor() as cursor:
                # Check if user exists
                cursor.execute("SELECT id FROM users WHERE email = %s", (email,))
                result = cursor.fetchone()

                if result:
                    return result[0]
                else:
                    # Create user if not exists
                    cursor.execute("INSERT INTO users (email) VALUES (%s)", (email,))
                    connection.commit()
                    return cursor.lastrowid
        except mysql.connector.Error as e:
            # It's good practice to log the error e for debugging
            raise Exception("Database error")