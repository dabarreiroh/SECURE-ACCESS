from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from core import test_audio as audio
from core import uploads3 as upload

def index(request):
    return render(request, 'home/audio.html')
def start(request):
    audio.audio()
    upload.upload('grabacion.wav','grabacion.wav')
    HttpResponse("Good REQUEST")
    return render(request, 'home/startaudio.html')




# Create your views here.
