from django.http import HttpResponse,Http404
from time import ctime
import datetime
def hello(request):
    return HttpResponse('Hello world')
def index(request):
    return HttpResponse('<html><body><p>time: %s </p></body></html>' % ctime())
def hour_ahead(request,offset):

    try:
        offset=int(offset)
    except ValueError:
        raise Http404
    dt=datetime.datetime.now()+datetime.timedelta(hours=offset)
    html="<html><body> %s hours later,time it is %s </body></html>" % (offset,dt)
    return HttpResponse(html)