from peewee import *

db = SqliteDatabase('main.db')

class User(Model):
    user_id = IntegerField(unique=True)
    username = CharField(null= True)
    status = TextField(null=True)
    class Meta:
        database = db

def create_tables():
    db.connect()
    User.create_table()

def user_exist(user_id):
    if len(User.select().where(User.user_id == user_id)) > 0:
        return True
    else:
        return False

def insert_user(user_id, username):
    user = User(user_id = user_id, username = username, status = 0)
    user.save()

def set_status(user_id, status):
    user = User.get(user_id = user_id)
    user.status = status
    user.save()

def get_status(user_id):
    return User.get(user_id = user_id).status