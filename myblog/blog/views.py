from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    response = render(request, 'blog/index.html')
    return response


def get_category(request):
    return render(request, 'blog/index.html')
