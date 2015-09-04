from pymarkovchain import MarkovChain
from threading import Lock

class Homestarkov(object):
    def __init__(self, path, character_name, tagline):
        self.path = path
        self.character_name = character_name
        self.tagline = tagline
        self._generator = MarkovChain("./markov-%s" % path)
        self._generator.generateDatabase("".join(self.quotes()))
        self._lock = Lock()

    def quotes(self):
        try:
            with open(self.path + ".txt") as corpus_file:
                return corpus_file.readlines()
        except IOError:
            return []

    def new_string(self):
        with self._lock:
            return self._generator.generateString()

    def json_object(self):
        return {
            "name": self.character_name,
            "path": self.path,
            "tagline": self.tagline
        }
