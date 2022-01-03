import pickle
import random
import nltk

from nltk import TrigramTagger, BigramTagger, UnigramTagger
from nltk.chunk import tree2conlltags,conlltags2tree
from nltk.corpus import conll2000
from nltk.corpus.reader.chasen import test
from train_pos_vnese import backoff_tagger
from nltk.chunk import ChunkParserI

def read_file(filename):
    corpus_line = ""

    with open(filename) as file:
        for line in file:
            corpus_line = corpus_line + line
    file.close()

    return corpus_line

def creat_corpus(corpus_line):
    corpus = []
    for line in corpus_line.split('\n\n'):
        sentence=[]
        for l in line.split('\n'):
            any = l.split(' ')
            tuple = (any[0],any[1],any[2])
            sentence.append(tuple)
        corpus.append(sentence)

    return corpus

corpus = creat_corpus(read_file('./model/vietnamese/corpus_chunk.txt'))
cuttof = int(len(corpus) * 0.8)
traindata = corpus[:cuttof]
testdata  = corpus[cuttof:]


nltk.download('conll2000')
shuffled_conll_sents = list(conll2000.chunked_sents())
random.shuffle(shuffled_conll_sents)

train_sents = shuffled_conll_sents[:int(len(shuffled_conll_sents) * 0.9)]
test_sents = shuffled_conll_sents[int(len(shuffled_conll_sents) * 0.9 + 1):]

test_data = [
    [(s[1], s[2]) for s in sent]
    for sent in testdata]
# print(test_data)

train_data = [
    [(s[1], s[2]) for s in sent]
    for sent in traindata]
print(train_data[0].__format__)
print('own train')
print(traindata[0].__format__)

t1 = UnigramTagger(train_data)
t2 = BigramTagger(train_data, backoff=t1)
tagger = TrigramTagger(train_data, backoff=t2)
a = tagger.evaluate(test_data)
print(a)

path = ("./model/vietnamese/chunker_trained.pkl")
with open(path, "wb") as f:
    pickle.dump(tagger, f)