from django.shortcuts import render
from django.http import JsonResponse 

# Create your views here.

def keyboard(request):
    return JsonResponse(
        {
            'type': 'button',
            'button' : ['test1', 'test2','test3']
        }
    )