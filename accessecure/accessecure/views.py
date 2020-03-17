from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.http import JsonResponse


def index(request):
    #template = loader.get_template('accessecure/templates/base.html')
    return render(request,'home/index.html')
    #return HttpResponse("hola")