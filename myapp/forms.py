from django import forms
from .models import About

class Aboutf(forms.ModelForm):
    class Meta:
        model=About
        fields=['name','contact','email','suggestions']
        widgets={
            'name':forms.TextInput(attrs={'placeholder':'Enter yor name'}),
            'contact':forms.TextInput(attrs={'placeholder':'Contact number'}),
            'email':forms.TextInput(attrs={'placeholder':'Enter your email'}),
            'suggestions':forms.Textarea(attrs={'placeholder':'Please Enter yor suggestions'}),
        }