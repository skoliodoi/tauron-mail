from .database import connection


class User:
    def __init__(self, id):
        cursor = connection.cursor()
        query = f"SELECT TOP 1 * FROM Tauron_Users WHERE user_login = '{id}'"
        cursor.execute(query)
        dane = cursor.fetchone()
        print(dane)
        self.id = dane[0]
        self.name = dane[1]
        self.last_name = dane[2]
        self.przelozony = dane[3]
        self.numer = dane[4]
        self.mail = dane[5]

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.id)
