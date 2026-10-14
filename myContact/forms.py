from django import forms
from django.forms import Form, CharField, EmailField, Textarea
from django.forms.models import ModelForm

from myContact.models import Contact  


class contactform2(Form):
        firstname=forms.CharField()
        lastname=forms.CharField()
        email=forms.EmailField()
        message=forms.CharField(widget=forms.Textarea)


class contactform3(ModelForm):
    class Meta:
        model = Contact
        fields = ['firstname', 'lastname', 'email', 'message']

class contactform(forms.Form):
     form_email = forms.EmailField(required=True)
     subject = forms.CharField(required=True)
     message = forms.CharField(widget=forms.Textarea, required=True)