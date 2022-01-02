from django.http.response import HttpResponse
from django.shortcuts import render
import model.english_train_chunker
from model.test import PostagChunkParser
# Create your views here.

def index(request):
    return render(request, 'index.html')

def vietnamese(request):
    return None

def english(request):
    model_pos='pos_trained.pkl'
    model_chunk='chunk_trained.pkl'
    chunker=PostagChunkParser(model_chunk,model_pos)
    #print(chunker.parse(input_text))

    if request.method == 'POST':
        input_text = request.POST['text']
        # chunker=PostagChunkParser(model_chunk,model_pos)
        print(input_text)
        print(chunker.parse(input_text))
        return render(request, 'englishdone.html', {'tree':chunker.parse(input_text)})

    return render(request, 'english.html', {'tree':chunker.parse('')})