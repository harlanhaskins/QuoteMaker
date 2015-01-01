from pymarkovchain import MarkovChain
from threading import Lock

class Homestarkov(object):
    def __init__(self, character_name):
        self.character_name = character_name
        self._generator = MarkovChain("./markov-%s" % character_name)
        self._generator.generateDatabase("".join(self.quotes()))
        self._lock = Lock()

    def quotes(self):
        try:
            with open(self.character_name + ".txt") as corpus_file:
                return corpus_file.readlines()
        except IOError:
            return []

    def new_string(self):
        with self._lock:
            return self._generator.generateString()

