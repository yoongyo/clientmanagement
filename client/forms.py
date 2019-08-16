from django import forms
from .models import Client


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['name', 'phone', 'content', 'birth', 'agent', 'address', 'agent_phone', 'joining_date', 'division',
                  'note1', 'note2', 'note3', 'registration_date', 'resident_registration_number', 'call_plane']
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
            'agent': forms.TextInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'address': forms.TextInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'agent_phone': forms.TextInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'joining_date': forms.TextInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'division': forms.TextInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'note1': forms.TextInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'note2': forms.TextInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'note3': forms.TextInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'registration_date': forms.TextInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'resident_registration_number': forms.TextInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'call_plane': forms.TextInput(
                attrs={
                    'class': 'form-control',
                }
            ),
        }


