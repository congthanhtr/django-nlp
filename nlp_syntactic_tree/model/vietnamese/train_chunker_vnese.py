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
cuttof = int(len(corpus) * 0.9)
traindata = corpus[:cuttof]
testdata  = corpus[cuttof:]

test_data = [
    [(s[1], s[2]) for s in sent]
    for sent in testdata]
# print(test_data)

train_data = [
    [(s[1], s[2]) for s in sent]
    for sent in traindata]

t1 = UnigramTagger(train_data)
t2 = BigramTagger(train_data, backoff=t1)
tagger = TrigramTagger(train_data, backoff=t2)
a = tagger.evaluate(test_data)
print(a)

path = ("./model/vietnamese/chunker_trained.pkl")
with open(path, "wb") as f:
    pickle.dump(tagger, f)