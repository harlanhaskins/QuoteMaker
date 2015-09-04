from pymarkovchain import MarkovChain
from pylru import lrudecorator
from peewee import *

db = SqliteDatabase('homestarkov.db', threadlocals=True)

class MarkovCache(object):
    @classmethod
    @lrudecorator(100)
    def get(cls, path):
        query = Homestarkov.select().where(Homestarkov.path == path)
        if not query.exists():
            return None
        character = query.first()
        _generator = MarkovChain("./markovgeneratorfiles/markov-%s" % path)
        _generator.generateDatabase(character.corpus)
        return _generator

class BaseModel(Model):
    class Meta:
        database = db

class Homestarkov(BaseModel):
    path = CharField(unique=True)
    name = CharField()
    tagline = CharField()
    corpus = TextField()

    def new_string(self):
        return MarkovCache.get(self.path).generateString()

    def json_object(self):
        return {
            "name": self.name,
            "path": self.path,
            "tagline": self.tagline
        }

db.connect()
Homestarkov.create_table(fail_silently=True)
