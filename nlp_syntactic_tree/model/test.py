import nltk
import pickle
import string
from nltk.chunk import ChunkParserI
from nltk.chunk import tree2conlltags,conlltags2tree
from nltk import pos_tag, word_tokenize

text = "Maybe i'm a little stuffy, but i wouldn't sell them, sniffs Bob Machon , owner of Papa 's Sports Cards inMenlo Park, Calif."
def load_model(path_name):
    f = open(path_name, 'rb')
    tagger = pickle.load(f)
    f.close()
    return tagger 

class PostagChunkParser(ChunkParserI):
    def __init__(self, model_chunk, model_pos=None):
        self.chunker = load_model(model_chunk)
        if model_pos:
            self.tagger = load_model(model_pos)
        else:
            self.tagger = None

    def parse(self, sentence):
        if isinstance(sentence, str):
            if self.tagger:
                words = word_tokenize(sentence)
                #remove punctuations
                punctuations = list(string.punctuation)
                words = [word for word in words if word not in punctuations]
                #pos_tag
                sentence = self.tagger.tag(words)
            else:#in case model doesnt work, using library function like a back up :>
                sentence = pos_tag(word_tokenize(sentence))
        
        pos_tags = [pos for word, pos in sentence]

        # Get the Chunk tags
        tagged_pos_tags = self.chunker.tag(pos_tags)

        # Assemble the (word, pos, chunk) triplets
        iob_triplets = [(word, pos_tag, chunk_tag)
                        for ((word, pos_tag), (pos_tag, chunk_tag)) in
                        zip(sentence, tagged_pos_tags)]

        # Transform the list of triplets to nltk.Tree format (Convert the CoNLL IOB format to a tree.)
        return conlltags2tree(iob_triplets)

model_pos='./model/english/pos_trained.pkl'
model_chunk='./model/english/chunk_trained.pkl'


chunker=PostagChunkParser(model_chunk,model_pos)
result= chunker.parse(text)
# print(result)
# result.draw()