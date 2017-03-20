from gensim.models import word2vec

sentences = [ "the quick brown fox jumps over the lazy dogs","yoyoyo you go home now to sleep"]
vocab = [s.encode('utf-8').split() for s in sentences]
model = word2vec.Word2Vec(vocab, min_count=1)
print model
print vocab
print model.wv.most_similar(positive=['fox', 'quick'], negative=['dogs'])
print model.wv.similarity('fox', 'dogs')
