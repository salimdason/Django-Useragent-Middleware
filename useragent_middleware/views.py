from django.shortcuts import render
from django.http import HttpResponse
from .exceptions import CustomException

def demo(request):
    if request.method == 'GET':
        return HttpResponse('How are you?')
    else:
        raise CustomException("Not to worry, this is just a demo.")


