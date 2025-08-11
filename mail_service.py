import MySQLdb
from datetime import datetime

class SendMail:
    def __init__(self):
        self.conn = MySQLdb.connect(
            host="localhost",
            user="root",
            passwd="Aspire@123",
            db="email_app_db"
        )
        self.cursor = self.conn.cursor()

    def send_mail(self, sender_email):
        print("\n--- Compose & Send Email ---")
        try:
            # Verify sender email exists in users table
            self.cursor.execute("SELECT email FROM users WHERE email=%s", (sender_email,))
            sender = self.cursor.fetchone()
            if not sender:
                print(" Sender email not registered.")
                return

            # Verify recipient email exists in users table
            recipient_email = input("Enter Recipient Email: ").strip()
            self.cursor.execute("SELECT email FROM users WHERE email=%s", (recipient_email,))
            recipient = self.cursor.fetchone()
            if not recipient:
                print(" Recipient email not registered.")
                return

            # Email content
            subject = input("Enter Subject: ")
            body = input("Enter Message Body: ")

            # Privacy mode
            is_private_input = input("Enable Privacy Mode? (y/n): ").strip().lower()
            is_private = is_private_input == 'y'

            expiry_date = None
            if is_private:
                expiry_input = input("Enter Expiry Date (YYYY-MM-DD HH:MM) or leave blank: ").strip()
                if expiry_input:
                    try:
                        expiry_date = datetime.strptime(expiry_input, "%Y-%m-%d %H:%M")
                    except ValueError:
                        print(" Invalid datetime format. Skipping expiry date.")

            # Insert email record directly with emails (no user IDs)
            query = """
                INSERT INTO emails (sender_email, recipient_email, subject, body, is_private, expiry_date)
                VALUES (%s, %s, %s, %s, %s, %s)
            """
            self.cursor.execute(query, (sender_email, recipient_email, subject, body, is_private, expiry_date))
            self.conn.commit()

            print(" Email sent successfully.")

        except Exception as e:
            print(" Error:", e)

    def close(self):
        self.cursor.close()
        self.conn.close()
