import MySQLdb
from datetime import datetime

class InboxReader:
    def __init__(self):
        self.conn = MySQLdb.connect(
            host="localhost",
            user="root",
            passwd="Aspire@123",
            db="email_app_db"
        )
        self.cursor = self.conn.cursor()

    def read_inbox(self, user_email):
        # Delete expired private emails first
        now = datetime.now()
        delete_query = """
            DELETE FROM emails
            WHERE recipient_email=%s AND is_private=1 AND expiry_date IS NOT NULL AND expiry_date < %s
        """
        self.cursor.execute(delete_query, (user_email, now))
        self.conn.commit()

        # Fetch emails sent to this recipient_email
        select_query = """
            SELECT sender_email, subject, body, is_private, expiry_date, created_at
            FROM emails
            WHERE recipient_email = %s
            ORDER BY created_at DESC
        """
        self.cursor.execute(select_query, (user_email,))
        emails = self.cursor.fetchall()

        if not emails:
            print(" Inbox is empty.")
            return

        print("\n--- Inbox ---")
        for sender_email, subject, body, is_private, expiry_date, created_at in emails:
            print(f"From: {sender_email}")
            print(f"Subject: {subject}")
            if is_private:
                print("**This is a private email**")
                if expiry_date:
                    print(f"Expires on: {expiry_date}")
            print(f"Sent at: {created_at}")
            print(f"Message: {body}")
            print("-" * 40)

    def close(self):
        self.cursor.close()
        self.conn.close()
