from peewee import *

db = SqliteDatabase('homestarkov.db', threadlocals=True)

class BaseModel(Model):
    class Meta:
        database = db
