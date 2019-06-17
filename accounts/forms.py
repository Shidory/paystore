from django import forms
from .models import *
from django.core.validators import validate_email
#from django.contrib.auth import get_user_model
#User = get_user_model()

class LoginForm(forms.ModelForm):
    email = forms.CharField(widget=forms.EmailInput(
        attrs={'class': 'form-control', 'placeholder': 'E-mail'}
    ), required=True, max_length=50)
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Password'}
    ), required=True, max_length=50)

    class Meta:
        model = UserLogin
        fields = [
            'email',
            'password'
        ]

    def clean_email(self):
        email = self.cleaned_data['email']
        try:
            mail = validate_email(email)
        except:
            return forms.ValidationError("Email is not in correct format")

    def clean_password(self):
        password = self.cleaned_data['email']
        min_lenght = 8
        if len(password) < min_lenght:
            raise forms.ValidationError("Password should have atleast %d characters!" % min_lenght)
        if password.isdigit():
            raise forms.ValidationError("Password should not all numeric")