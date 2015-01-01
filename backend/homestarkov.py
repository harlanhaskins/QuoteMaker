from pymarkovchain import MarkovChain

class Homestarkov(object):
    def __init__(self, character_name):
        self.character_name = character_name
        self._generator = MarkovChain("./markov-%s" % character_name)
        self._generator.generateDatabase("".join(self.quotes()))

    def quotes(self):
        try:
            with open(self.character_name + ".txt") as corpus_file:
                return corpus_file.readlines()
        except IOError:
            return []

    def new_string(self):
        return self._generator.generateString()

