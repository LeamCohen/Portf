from django import forms
from django.core.validators import EmailValidator

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, 
            widget=forms.TextInput(attrs={'placeholder' : "Full Name"}))
    email = forms.CharField(validators=[EmailValidator()],
            widget=forms.TextInput(attrs={'placeholder' : "Email"}))
    phonenum = forms.CharField(max_length=15,
            widget=forms.TextInput(attrs={'placeholder' : "Phone Number"}))
    subject = forms.CharField(max_length=100,
            widget=forms.TextInput(attrs={'placeholder' : "Subject"}))
    message = forms.CharField(widget=forms.Textarea(attrs={'placeholder' : "Message"}))