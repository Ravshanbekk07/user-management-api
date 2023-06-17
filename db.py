from tinydb import TinyDB,Document
from tinydb.table import Document
db = TinyDB("../db.json", indent=4)


class DB:
    def __init__(self):
        self.users = db.table("users")

    def get_all_users(self):
        return self.users.all()

    def get_user_by_id(self, chat_id):
        return self.users.get(doc_id=chat_id)

    def create_user(self, first_name: str, last_name: str, username: str,chat_id:int):
        user = Document({"firstname": first_name, "lastname": last_name, "username": username},doc_id=chat_id)
        return self.users.insert(user)

    def update(self, chat_id, first_name: str, last_name: str, username: str):
        return self.users.update(
            {"firstname": first_name, "lastname": last_name, "username": username},
            doc_ids=[chat_id]
        )

    def delete(self, chat_id):
        return self.users.remove(doc_ids=[chat_id])
