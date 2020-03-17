
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from core import test_camera as camera
from core import uploads3 as upload


def index(request):
    camera.camera()
    upload.upload('media/foto.png','foto.png')
    return render(request,'home/photo.html')


def home(request):
    #template = loader.get_template('accessecure/templates/base.html')
    return render(request,'thanks.html')

def photo(request):
    return JsonResponse({'url': 'urls',
                         "public_id": 'publicid',
                         "domain": 'domain'
                         })
def dbi_service(request):
    pass
def dbi_crud_keywords(request):
    pass
def dbi_query_keywords(request):
    pass

