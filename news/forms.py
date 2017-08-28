from django import forms
from .models import Form

class ContactForm(forms.ModelForm):
    class Meta:
        model = Form
        fields = ['name','email','number','message']
    #name = forms.CharField(label='Name', max_length=100)
    #email = forms.EmailField(label='Email Address')
    #number = forms.CharField(label='Phone Number', max_length=20)
    #message = forms.CharField(widget=forms.Textarea, label='Message', max_length=2000)
