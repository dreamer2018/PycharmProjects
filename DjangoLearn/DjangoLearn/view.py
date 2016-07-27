
from django.http import HttpResponse,Http404
from django.shortcuts import render_to_response
from django.template.loader import get_template
from django.template import Context
import datetime
from time import ctime
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
def temp_time(request):
    now = datetime.datetime.now()
    t=get_template('temp.html')
    html = t.render(Context({ 'current_date':now }))
    return HttpResponse(html)
def temp_simp(request):
    now = ctime()
    return render_to_response('temp.html',{'current_date':now})