from flask_login import UserMixin
from src.executeQuerys import getQueryData

class User(UserMixin):
    def __init__(self, id: str, username: str, password: str, role: str):
        self.id = id
        self.username = username
        self.password = password
        self.role = role
    
    @staticmethod
    def getByUsername(username: str):
        data = getQueryData("SELECT id,usuario,password_hash,role FROM Usuario WHERE usuario = ?", (username,))
        if len(data) > 0:
            return User(data[0]['id'], data[0]['usuario'], data[0]['password_hash'], data[0]['role'])
        return None
    
    def get(user_id: str):
        data = getQueryData("SELECT id,usuario,password_hash,role FROM Usuario WHERE id = ?", (user_id,))
        if len(data) > 0:
            return User(data[0]['id'], data[0]['usuario'], data[0]['password_hash'], data[0]['role'])
        return None

    def __str__(self) -> str:
        return f"<Id: {self.id}, Username: {self.username}, Role: {self.role}>"

    def __repr__(self) -> str:
        return self.__str__()