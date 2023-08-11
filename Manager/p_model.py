from sqlalchemy import create_engine,Column,Integer,String
from sqlalchemy.ext.declarative import declarative_base
from cryptography.fernet import Fernet
from sqlalchemy.orm import validates

Base = declarative_base()

def generate_key():
    return Fernet.generate_key()

class PasswordManager(Base):
    __tablename__ = 'Details'
    id = Column(Integer,primary_key=True)
    name =Column(String(100),nullable=False)
    email =Column(String(100),nullable=False)
    account=Column(String(100),nullable=False)
    password=Column(String(200),nullable=False)


    Encryption_key = generate_key()
    with open('key.txt','a') as file:
        file.writelines(str(Encryption_key))

    @validates('password')
    def validate_encrypted_password(self,key,value):
        fernet = Fernet(self.Encryption_key)
        return fernet.encrypt(value.encode())

    def get_decrypted_password(self):
        fernet = Fernet(self.Encryption_key)
        return fernet.decrypt(self.password.encode()).decode()



# Replace 'username', 'password', 'hostname', and 'database_name' with your MySQL credentials
engine = create_engine('mysql+mysqlconnector://username:password@hostname/database_name')
Base.metadata.create_all(engine)