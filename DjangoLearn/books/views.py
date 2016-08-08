from django.core.mail import send_mail
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect

from books.models import Book


# Create your views here.
def search_form(request):
    return render_to_response('search_form.html')


def search(request):
    # if 'q' in request.GET:
    #     message = 'Your Search for : %s ' % request.GET['q']
    # else:
    #     message = 'Your Submit Empty！'
    # return HttpResponse(message)
    error = False
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            error = True
        else:
            books = Book.objects.filter(title__icontains=q)
            return render_to_response('search_result.html', {'books': books, 'query': q})
    # return HttpResponse('Please submit a search term.')
    return render_to_response('search_form.html', {'error': error})


def contact(request):
    errors = []
    if request.method == 'POST':
        if not request.POST.get('subject', ''):
            errors.append('input subject!')
        if not request.POST.get('message', ''):
            errors.append('input message')
        if request.POST.get('email') and '@' not in request.POST['email']:
            errors.append('input a valid e-mail address!')
        if not errors:
            send_mail(
                request.POST['subject'],
                request.POST['message'],
                request.POST.get('email', 'noreply@example.com'),
                ['siteowner@example.com'],
            )
            return HttpResponseRedirect('/contact/thanks/')
    return render_to_response('contact_form.html',{'errors':errors,
                                                   'subject':request.POST.get('subject',''),
                                                   'message':request.POST.get('message',''),
                                                   'email':request.POST.get('email',''),
                                                   })

