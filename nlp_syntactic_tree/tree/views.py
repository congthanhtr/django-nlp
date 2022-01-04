from django.http.response import HttpResponse
from django.shortcuts import render
from underthesea.pipeline.word_tokenize import model
# import model.english_train_chunker
# import model.vietnamese.train_chunker_vnese
from model.test import PostagChunkParser
from model.vietnamese_test import VNPostagChunkParser
# Create your views here.

def index(request):
    return render(request, 'index.html')

def vietnamese(request):
    model_pos='./model/vietnamese/pos_trained.pkl'
    model_chunk='./model/vietnamese/chunker_trained.pkl'
    chunker=VNPostagChunkParser(model_chunk,model_pos)
    #print(chunker.parse(input_text))

    if request.method == 'POST':
        input_text = request.POST['text']
        # chunker=PostagChunkParser(model_chunk,model_pos)
        return render(request, 'vietnamesedone.html', {'tree':chunker.parse(input_text), 'sentence': input_text})

    return render(request, 'vietnamese.html', {'tree':chunker.parse('')})

def english(request):
    model_pos='./model/english/pos_trained.pkl'
    model_chunk='./model/english/chunk_trained.pkl'
    chunker=PostagChunkParser(model_chunk,model_pos)
    #print(chunker.parse(input_text))

    if request.method == 'POST':
        input_text = request.POST['text']
        # chunker=PostagChunkParser(model_chunk,model_pos)
        return render(request, 'englishdone.html', {'tree':chunker.parse(input_text), 'sentence': input_text})

    return render(request, 'english.html', {'tree':chunker.parse('')})