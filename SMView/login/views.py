from django.shortcuts import render_to_response


# Create your views here.


def index(requset):
    render = {
        'url': '..'
    }
    return render_to_response('login.html', render)


def login(request):
    request.encoding = 'utf-8'
