import gensim, logging
import os

class MySentences(object):
    def __init__(self, dirname):
        self.dirname = dirname

    def __iter__(self):
        for fname in os.listdir(self.dirname):
            for line in open(os.path.join(self.dirname, fname)):
                yield line.split()

sentences = MySentences('/Users/vanessaputnam/words') # a memory-friendly iterator
model = gensim.models.Word2Vec(sentences,min_count=1)
print model
