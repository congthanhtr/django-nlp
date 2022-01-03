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

# def conll_tag_chunks(chunk_data):
      
#     # tagged_data = [tree2conlltags(tree) for 
#     #                 tree in chunk_data]
      
#     return [[(t, c) for (w, t, c) in sent] 
#             for sent in chunk_data]
      
# class TagChunker(ChunkParserI):
      
#     def __init__(self, train_chunks, 
#                  tagger_classes =[UnigramTagger, BigramTagger]):
          
#         train_data = conll_tag_chunks(train_chunks)
#         self.tagger = backoff_tagger(train_data, tagger_classes)
          
#     def parse(self, tagged_sent):
#         if not tagged_sent: 
#             return None
          
#         (words, tags) = zip(*tagged_sent)
#         chunks = self.tagger.tag(tags)
#         wtc = zip(words, chunks)
          
#         return conlltags2tree([(w, t, c) for (w, (t, c)) in wtc])

corpus = creat_corpus(read_file('./model/vietnamese/corpus_chunk.txt'))
cuttof = int(len(corpus) * 0.8)
traindata = corpus[:cuttof]
testdata  = corpus[cuttof:]

# chunker = TagChunker(traindata, tagger_classes=[UnigramTagger])
# score = chunker.evaluate(testdata)


# a = score.accuracy()
# p = score.precision()
# r = recall
  
# print ("Accuracy of TagChunker : ", a)
# print ("\nPrecision of TagChunker : ", p)
# print ("\nRecall of TagChunker : ", r)

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