from django import forms
from .models import ContactMsg

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMsg
        fields =  ['name','email','message']
        widgets = { 'name' : forms.TextInput(attrs={'class':'form-control'}),
                  'email' : forms.EmailInput(attrs={'class':'form-control'}),
                  'message' : forms.Textarea(attrs={'class':'form-control', 'rows':'5'}),
                  }