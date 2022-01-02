# import pickle
# import random
# import nltk

# from nltk import TrigramTagger, BigramTagger, UnigramTagger
# from nltk.chunk import tree2conlltags,conlltags2tree
# from nltk.corpus import conll2000
# from model.english_train_pos import backoff_tagger
# from nltk.tokenize import word_tokenize

# # initializing training and testing set
# nltk.download('conll2000')
# shuffled_conll_sents = list(conll2000.chunked_sents())
# random.shuffle(shuffled_conll_sents)

# train_sents = shuffled_conll_sents[:int(len(shuffled_conll_sents) * 0.9)]
# test_sents = shuffled_conll_sents[int(len(shuffled_conll_sents) * 0.9 + 1):]

# # Extract only the (POS-TAG, IOB-CHUNK-TAG) pairs
# train_data = [
#     [(pos_tag, chunk_tag) for word, pos_tag, chunk_tag in tree2conlltags(sent)]
#     for sent in train_sents]
# test_data = [
#     [(pos_tag, chunk_tag) for word, pos_tag, chunk_tag in tree2conlltags(sent)]
#     for sent in test_sents]

# '''
# t = Tree('S', [Tree('NP', [('the', 'DT'), ('book', 'NN')])])
# >>> tree2conlltags(t)
# [('the', 'DT', 'B-NP'), ('book', 'NN', 'I-NP')]
# >>> conlltags2tree([('the', 'DT', 'B-NP'), ('book', 'NN', 'I-NP')])
# Tree('S', [Tree('NP', [('the', 'DT'), ('book', 'NN')])])
# '''

# # Train a NgramTagger
# t1 = UnigramTagger(train_data)
# t2 = BigramTagger(train_data, backoff=t1)
# tagger = TrigramTagger(train_data, backoff=t2)
# #a = tagger.evaluate(test_data)

# #print("Accuracy of postag tagger: ", a)  # 0.8925600739371534

# # save pickle
# path = ("chunk_trained.pkl")

# with open(path, "wb") as f:
#     pickle.dump(tagger, f)