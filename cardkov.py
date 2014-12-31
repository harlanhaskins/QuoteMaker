from pymarkovchain import MarkovChain

corpus_filename = 'cardpus.txt'

def quotes():
    with open(corpus_filename) as corpus_file:
        return corpus_file.readlines()

def new_string():
    return mc.generateString()

mc = MarkovChain("./markov")
mc.generateDatabase("".join(quotes()))

print new_string()
