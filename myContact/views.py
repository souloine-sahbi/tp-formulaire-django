from http.client import HTTPResponse

from django.core.mail import send_mail
from django.http import BadHeaderError, HttpResponse, request
from django.shortcuts import redirect, render

from myContact.forms import contactform, contactform2, contactform3
from myContact.models import Contact


def controleform1(request):
    if request.method == 'POST':
        f=request.POST['firstname']
        l=request.POST['lastname']
        e=request.POST['email']
        m=request.POST['message']
        contact=Contact.objects.create(firstname=f,lastname=l,email=e,message=m)
        return HttpResponse('<h2> Data has been submitted </h2>')
    return render(request,"myform1.html")

def controleform2(request):
    form=contactform2(request.POST)

    if request.method == 'POST':
        if form.is_valid():
            f=form.cleaned_data['firstname']
            l=form.cleaned_data['lastname']
            e=form.cleaned_data['email']
            m=form.cleaned_data['message']
            contact=Contact.objects.create(firstname=f,lastname=l,email=e,message=m)
            return HttpResponse('<h2> Data has been submitted </h2>')
        else:
            form=contactform2()
    return render(request,"myform2.html",{'mycontactform2':form})

def controleform3(request):
    if request.method == 'POST':
        form=contactform3(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('<h2> Data has been submitted </h2>')
    else:
        form=contactform3()
    return render(request,"myform3.html",{'mycontactform3':form})

def contactView(request):
    if request.method == 'GET': form = contactform()
    else: 
        form = contactform(request.POST) 
        if form.is_valid(): 
            subject = form.cleaned_data['subject']
            form_email = form.cleaned_data['form_email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, form_email, ['sahbisouloi@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
        return redirect('success')
    return render(request, "email.html", {'form': form})

def successView(request):
    return HttpResponse('Success! Thank you for your message.')
        
        