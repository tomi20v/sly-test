import mysql.connector

class UserRepository:
    def __init__(self, db):
        self.db = db

    def get_or_create_by_email(self, email: str) -> int:
        """
        Finds a user by email. If the user does not exist, it creates a new one.
        Returns the user ID.
        """
        try:
            connection = self.db.get_connection()
            with connection.cursor(dictionary=True) as cursor:
                # Find user by email
                cursor.execute("SELECT id FROM users WHERE email = %s", (email,))
                user = cursor.fetchone()

                if user:
                    return user['id']
                else:
                    # Create new user if not found
                    cursor.execute("INSERT INTO users (email) VALUES (%s)", (email,))
                    connection.commit()
                    return cursor.lastrowid
        except mysql.connector.Error as e:
            # Re-raise the exception to be handled by the resource
            raise e
