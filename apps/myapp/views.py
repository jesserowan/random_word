from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string

def index(request):
    if not 'counter' in request.session:
        request.session['counter'] = 0
    random = {
        "word": get_random_string(14),
    }
    if request.method == "GET":
        request.session['counter'] += 1
    return render(request, 'myapp/index.html', random)

def reset(request):
    if request.method == "GET":
        del request.session['counter']
    return redirect('/')