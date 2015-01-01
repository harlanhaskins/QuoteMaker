import sys
import re

regex = re.compile("^\|\s+\"(.*?)\"\n")

def create_corpus_from_table(character):
    filename = "%s_table.txt" % character
    with open(filename) as table_file:
        lines = table_file.readlines()[0::5]
        parsed = [regex.sub("\\1", q) for q in lines]
        with open(character + ".txt", "a+") as corpus_file:
            corpus_file.seek(0)
            corpus_file.write("\n".join(parsed))

create_corpus_from_table(sys.argv[1])
