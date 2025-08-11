from login_system import LoginSystem
from mail_service import SendMail
from inbox_reader import InboxReader

def main():
    login_system = LoginSystem()
    mailer = SendMail()
    inbox = InboxReader()

    while True:
        print("\n--- Main Menu ---")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Enter choice: ")

        if choice == '1':
            login_system.registerUser()

        elif choice == '2':
            user = login_system.loginUser()
            if user:
                print(f"Welcome, {user['username']}!")

                while True:
                    print("\n--- User Menu ---")
                    print("1. Compose and Send Email")
                    print("2. Read Inbox")
                    print("3. Logout")
                    sub_choice = input("Enter choice: ")

                    if sub_choice == '1':
                        mailer.send_mail(user['email'])
                    elif sub_choice == '2':
                        inbox.read_inbox(user['email'])
                    elif sub_choice == '3':
                        print("Logging out...")
                        break
                    else:
                        print("Invalid choice. Please select 1, 2, or 3.")

        elif choice == '3':
            print("Exiting...")
            login_system.closeConnection()
            mailer.close()
            inbox.close()
            break

        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
