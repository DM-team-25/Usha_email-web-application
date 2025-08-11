import MySQLdb
import re
import pwinput

class LoginSystem:
    def __init__(self):
        self.conn = MySQLdb.connect(
            host="localhost",
            user="root",
            passwd="Aspire@123",
            db="email_app_db"
        )
        self.cursor = self.conn.cursor()

    def validateUsername(self, username):
        return re.match(r'^[A-Za-z][A-Za-z0-9_]{5,19}$', username)

    def validatePassword(self, password):
        return re.match(r'^[A-Za-z0-9@#$%^&+=]{6}$', password)

    def validateEmail(self, email):
        return re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email)

    def registerUser(self):
        print("\n--- Register ---")
        while True:
            username = input("Enter username: ")
            if self.validateUsername(username):
                break
            print(" Username must start with a letter, be 6-20 characters, and use only letters, numbers, or _.")

        while True:
            password = pwinput.pwinput("Enter 6-char password: ", mask='*')
            if self.validatePassword(password):
                break
            print(" Password must be exactly 6 characters. Allowed: letters, numbers, @#$%^&+=")

        while True:
            email = input("Enter email: ")
            if self.validateEmail(email):
                break
            print(" Enter a valid email address.")

        try:
            self.cursor.execute(
                "INSERT INTO users (username, password, email) VALUES (%s, %s, %s)",
                (username, password, email)
            )
            self.conn.commit()
            print(" Registered successfully!")
        except MySQLdb.IntegrityError:
            print(" Username or email already exists.")

    def loginUser(self):
        print("\n--- Login ---")
        username = input("Enter username: ")
        password = pwinput.pwinput("Enter password: ", mask='*')

        self.cursor.execute(
            "SELECT id, username, email FROM users WHERE username=%s AND password=%s",
            (username, password)
        )
        result = self.cursor.fetchone()
        if result:
            print(" Login successful!")
            return {"id": result[0], "username": result[1], "email": result[2]}
        else:
            print(" Invalid username or password.")
            return None

    def closeConnection(self):
        self.cursor.close()
        self.conn.close()
