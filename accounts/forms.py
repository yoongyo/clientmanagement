from django.contrib.auth.forms import AuthenticationForm, UsernameField
from django import forms


class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(
        attrs={
            'id': 'username',
            'type': 'text',
            'class': 'mt-4 mb-0 form-control',
            'value': "",
            'required autofocus': True,
            'placeholder': '전화번호를 입력하세요',
            'autocomplete': 'off',
            'style': ''
        }
    ))
    password = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput(
            attrs={
                'value': 'aa728500',
                'id': 'password',
                'type': 'password',
                'class': 'mt-2',
                'placeholder': 'Password',
                'required data-eye': True,
                'autocomplete': 'off',
                'style': 'display:none'
            }
        ),
    )