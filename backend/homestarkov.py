from pymarkovchain import MarkovChain

class Homestarkov(object):
    def __init__(self, path, character_name, tagline):
        self.path = path
        self.character_name = character_name
        self.tagline = tagline
        self._generator = MarkovChain("./markov-%s" % path)
        self._generator.generateDatabase("".join(self.quotes()))

    def quotes(self):
        try:
            with open(self.path + ".txt") as corpus_file:
                return corpus_file.readlines()
        except IOError:
            return []

    def new_string(self):
        return self._generator.generateString()

    def json_object(self):
        return {
            "name": self.character_name,
            "path": self.path,
            "tagline": self.tagline
        }
