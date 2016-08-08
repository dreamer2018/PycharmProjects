from django.shortcuts import render_to_response
from django.shortcuts import HttpResponse

# Create your views here.
def search_form(request):
    return render_to_response('search_form.html')
def search(request):
    if 'q' in request.GET :
        message = 'Your Search for : %s ' % request.GET['q']
    else:
        message = 'Your Submit Empty！'
    return HttpResponse(message)
