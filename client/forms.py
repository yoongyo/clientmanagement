from django import forms
from .models import Client


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['name', 'phone', 'content']
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'phone': forms.TextInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'content': forms.Textarea(
                attrs={
                    'class': 'form-control',
                }
            ),
        }
