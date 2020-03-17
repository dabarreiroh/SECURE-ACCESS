from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.http import JsonResponse
from core import test_camera as camera
from core import uploads3 as upload

def index(request):
    #template = loader.get_template('accessecure/templates/base.html')
    return render(request,'home/index.html')
    #return HttpResponse("hola")
def verified(request):
    #template = loader.get_template('accessecure/templates/base.html')
    return render(request,'home/authenticated.html')
