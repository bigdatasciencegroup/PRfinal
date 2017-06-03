from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from django.shortcuts import redirect

app_name = 'webcam'

def index(request):
    context = {}
    return render(request, 'webcam/index.html', context)

def video(request):
    print (request.POST['content'])
    return redirect('/webcam/')
