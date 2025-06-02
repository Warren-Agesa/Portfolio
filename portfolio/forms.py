from django import forms
from .models import ContactMessage

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control rounded-pill'}),
            'email': forms.EmailInput(attrs={'class': 'form-control rounded-pill'}),
            'subject': forms.TextInput(attrs={'class': 'form-control rounded-pill'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
        }