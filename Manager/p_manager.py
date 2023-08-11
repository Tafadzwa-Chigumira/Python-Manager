from sqlalchemy.orm import sessionmaker
from p_model import PasswordManager,engine


def add_details(name,email,account,password):
    Session = sessionmaker(bind=engine)
    session = Session()

    Details = PasswordManager(name=name,email=email,account=account,password=password)
    session.add(Details)
    session.commit()
    print('Added Details Successfully')
    session.close()

def retrieve_details():
    Session = sessionmaker(bind=engine)
    session = Session()
    Details = session.query(PasswordManager)
    if not Details:
        print("Details not found")
    else:
        print("\nDetails in Database: ")
        for Detail in Details:
            decrypted_password = Detail.get_decrypted_password()
            print(f'Name: {Detail.name}\nEmail: {Detail.email}\nAccount:{Detail.account}\nPassword: {decrypted_password}')
    session.close()

if __name__ == '__main__':
    while True:
        print('\n1. Add Details\n2. Retrieve Details\n3. Exit')
        choice = input('\nEnter your choice: ')

        if choice == '1':
            name = input("Enter First name and Surname: ")
            email = input('Enter Email: ')
            account = input('Enter Account: ')
            password = input('Enter Password: ')
            add_details(name, email, account, password)

        elif choice == '2':
            retrieve_details()

        elif choice == '3':
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")
















