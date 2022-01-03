# import pickle
# import random
# import nltk

# from nltk.corpus import brown
# from nltk.tag import UnigramTagger, BigramTagger, TrigramTagger
# from nltk.tag import BrillTaggerTrainer, brill
# from nltk.tag.sequential import DefaultTagger

# '''Tagging sentences
# i also implements a tag_sents() method that can be used to tag a list of
# sentences, instead of a single sentence. Here's an example of tagging two simple sentences:
# >>> tagger.tag_sents([['Hello', 'world', '.'], ['How', 'are', 'you',
# '?']])
# [[('Hello', 'NN'), ('world', 'NN'), ('.', 'NN')], [('How', 'NN'),
# ('are', 'NN'), ('you', 'NN'), ('?', 'NN')]]
# The result is a list of two tagged sentences, and of course, every tag is NN because we're using
# the DefaultTagger class. The tag_sents() method can be quiet useful if you have many
# sentences you wish to tag all at once.
# '''

# '''Evaluating accuracy
# To know how accurate a tagger is, you can use the evaluate() method, which takes a list
# of tagged tokens as a gold standard to evaluate the tagger. Using our default tagger created
# earlier, we can evaluate it against a subset of the treebank corpus tagged sentences.
# >>> from nltk.corpus import treebank
# >>> test_sents = treebank.tagged_sents()[3000:]
# >>> tagger.evaluate(test_sents)
# 0.14331966328512843
# So, by just choosing NN for every tag, we can achieve 14 % accuracy testing on one-fourth
# of the treebank corpus. Of course, accuracy will be different if you choose a different
# default tag. We'll be reusing these same test_sents for evaluating more taggers in the
# upcoming recipes.
# '''

# '''UnigramTagger
# UnigramTagger builds a context model from the list of tagged sentences. Because
# UnigramTagger inherits from ContextTagger, instead of providing a choose_tag()
# method, it must implement a context() method, which takes the same three arguments as
# choose_tag(). The result of context() is, in this case, the word token. The context token
# is used to create the model, and also to look up the best tag once the model is created. Here's
# an inheritance diagram showing each class, starting at SequentialBackoffTagger:
# UnigramTagger->NgramTagger->ContextTagger{context()}->SequentialBackoffTagger{choose_tag()}
# '''

# '''Backoff tagging
# is one of the core features of SequentialBackoffTagger. It allows you
# to chain taggers together so that if one tagger doesn't know how to tag a word, it can pass
# the word on to the next backoff tagger. If that one can't do it, it can pass the word on to the
# next backoff tagger, and so on until there are no backoff taggers left to check.
# - to know how to do it and it works:  read page 95
# '''
# def backoff_tagger(tagged_sents, tagger_classes, backoff=None):
#     if not backoff:
#         backoff = tagger_classes[0](tagged_sents)
#         del tagger_classes[0]
 
#     for cls in tagger_classes:
#         tagger = cls(tagged_sents, backoff=backoff)
#         backoff = tagger
#     print("check:\n",backoff)
#     return backoff

# #backoff = DefaultTagger('NN')
# #tagger = backoff_tagger(train_sents, [UnigramTagger, BigramTagger,TrigramTagger], backoff=backoff)

# '''Training a Brill tagger
# The BrillTagger class is a transformation-based tagger. It is the first tagger that is not a
# subclass of SequentialBackoffTagger. Instead, the BrillTagger class uses a series
# of rules to correct the results of an initial tagger. These rules are scored based on how many
# errors they correct minus the number of new errors they produce.
# '''

# # initializing training and testing set
# nltk.download('brown')
# corpus = [_ for _ in brown.tagged_sents()]  # 57340

# print(len(corpus))
# print(corpus[0])
# random.shuffle(corpus)

# cuttof = int(len(corpus) * 0.9)
# train_data = corpus[:cuttof]
# test_data = corpus[cuttof:]

# def train_brill_tagger(initial_tagger, train_sents, **kwargs):
#     templates = [
#     brill.Template(brill.Pos([-1])),
#     brill.Template(brill.Pos([1])),
#     brill.Template(brill.Pos([-2])),
#     brill.Template(brill.Pos([2])),
#     brill.Template(brill.Pos([-2, -1])),
#     brill.Template(brill.Pos([1, 2])),
#     brill.Template(brill.Pos([-3, -2, -1])),
#     brill.Template(brill.Pos([1, 2, 3])),
#     brill.Template(brill.Pos([-1]), brill.Pos([1])),
#     brill.Template(brill.Word([-1])),
#     brill.Template(brill.Word([1])),
#     brill.Template(brill.Word([-2])),
#     brill.Template(brill.Word([2])),
#     brill.Template(brill.Word([-2, -1])),
#     brill.Template(brill.Word([1, 2])),
#     brill.Template(brill.Word([-3, -2, -1])),
#     brill.Template(brill.Word([1, 2, 3])),
#     brill.Template(brill.Word([-1]), brill.Word([1])),
#     ]
#     '''
#     The templates specify how to learn transformation rules. For example, brill.
#     Template(brill.Pos([-1])) means that a rule can be generated using the previous
#     part-of-speech tag. The brill.Template(brill.Pos([1])) statement means that you
#     can look at the next part-of-speech tag to generate a rule. And brill.Template(brill.
#     Word([-2, -1])) means you can look at the combination of the previous two words to
#     learn a transformation rule.
#     '''

#     trainer = BrillTaggerTrainer(initial_tagger,templates, deterministic=True)
#     '''
#     The job of BrillTaggerTrainer is to produce these rules, and to do so
#     in a way that increases accuracy. A transformation rule that fixes one problem may cause an
#     error in another condition; thus, every rule must be measured by how many errors it corrects
#     versus how many new errors it introduces.
#     '''
    
#     return trainer.train(train_sents,max_rules=100)


# #To use it, we can create our initial_tagger from a backoff chain of NgramTagger classes,
# #then pass that into the train_brill_tagger() function to get a BrillTagger back.
# default_tagger = DefaultTagger('NN')
# initial_tagger = backoff_tagger(train_data, [UnigramTagger,BigramTagger, TrigramTagger], backoff=default_tagger)
# print(initial_tagger.evaluate(test_data))
# #0.9245422455615643

# brill_tagger = train_brill_tagger(initial_tagger, train_data)
# print(brill_tagger.evaluate(test_data))
# #0.934897146533586
# #So, the BrillTagger class has slightly increased accuracy over the initial_tagger.

# # save pickle
# path =  "pos_trained.pkl"
# with open(path, "wb") as f:
#     pickle.dump(brill_tagger, f)


# #---------------------------------
# #testing:
# '''
# f = open(path, 'rb')
# tagger = pickle.load(f)
# f.close()
# text = "A journey of a thousand miles begins with a single step, said Lao Tzu."
# from nltk.tokenize import sent_tokenize
# from nltk import pos_tag, word_tokenize
# sentences = sent_tokenize(text)
# #print(len(sentences), 'sentences:', sentences)
# words = word_tokenize(text)
# #print(len(words), 'words:', words)
# import string
# punctuations = list(string.punctuation)
#     #print(punctuations)
# words = [word for word in words if word not in punctuations]
# pos_tagged_text = tagger.tag(words)
# print("Handmake result: ",pos_tagged_text)
# #sample_text = "The quick brown fox jumps over the lazy dog"
# tagged = pos_tag(words)
# #tagged = pos_tag(word_tokenize(text))
# print("Library result: ",tagged)
# '''