import pickle
import random
import nltk

from nltk.corpus import brown
from nltk.tag import UnigramTagger, BigramTagger, TrigramTagger
from nltk.tag import BrillTaggerTrainer, brill
from nltk.tag.sequential import DefaultTagger

def backoff_tagger(tagged_sents, tagger_classes, backoff=None):
    if not backoff:
        backoff = tagger_classes[0](tagged_sents)
        del tagger_classes[0]
 
    for cls in tagger_classes:
        tagger = cls(tagged_sents, backoff=backoff)
        backoff = tagger
    print("check:\n",backoff)
    return backoff

# # nltk.download('brown')
# # corpus = [_ for _ in brown.tagged_sents()]  # 5734
# # print(corpus[0])
def read_file(filename):
    corpus_line = ""

    with open(filename) as file:
        for line in file:
            corpus_line = corpus_line + line
    file.close()

    return corpus_line

def creat_corpus(corpus_line):
    corpus = []
    for line in corpus_line.splitlines():
        sentence = []
        for word in line.split():
            w = word.split('/')
            tuple = (w[0], w[1])
            sentence.append(tuple)
        corpus.append(sentence)
        # print(word)
        # w = word.split('/')
        # # print(w)
        # # tuple = (w[0], w[1])
        # # corpus.append(tuple)
    return corpus

# print(creat_corpus(read_file('cor')))
# print(creat_corpus(read_file('corpus.txt')))
corpus = creat_corpus(read_file('./model/vietnamese/corpus_pos.txt'))
cuttof = int(len(corpus) * 0.9)
train_data = corpus[:cuttof]
test_data = corpus[cuttof:]

def train_brill_tagger(initial_tagger, train_sents, **kwargs):
    templates = [
    brill.Template(brill.Pos([-1])),
    brill.Template(brill.Pos([1])),
    brill.Template(brill.Pos([-2])),
    brill.Template(brill.Pos([2])),
    brill.Template(brill.Pos([-2, -1])),
    brill.Template(brill.Pos([1, 2])),
    brill.Template(brill.Pos([-3, -2, -1])),
    brill.Template(brill.Pos([1, 2, 3])),
    brill.Template(brill.Pos([-1]), brill.Pos([1])),
    brill.Template(brill.Word([-1])),
    brill.Template(brill.Word([1])),
    brill.Template(brill.Word([-2])),
    brill.Template(brill.Word([2])),
    brill.Template(brill.Word([-2, -1])),
    brill.Template(brill.Word([1, 2])),
    brill.Template(brill.Word([-3, -2, -1])),
    brill.Template(brill.Word([1, 2, 3])),
    brill.Template(brill.Word([-1]), brill.Word([1])),
    ]

    trainer = BrillTaggerTrainer(initial_tagger,templates, deterministic=True)

    return trainer.train(train_sents,max_rules=100)

default_tagger = DefaultTagger('N')
# print(UnigramTagger)
initial_tagger = backoff_tagger(train_data, [UnigramTagger, BigramTagger, TrigramTagger], backoff=default_tagger)
print(initial_tagger.evaluate(test_data)) 

brill_tagger = train_brill_tagger(initial_tagger, train_data)
print(brill_tagger.evaluate(test_data))

path =  "./model/vietnamese/pos_trained.pkl"
with open(path, "wb") as f:
    pickle.dump(brill_tagger, f)