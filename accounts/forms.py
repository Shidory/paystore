from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Username'}
    ))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Password'}
    ))

    def clean_username(self):
        username = self.cleaned_data.get("username")
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise forms.ValidationError("Are you sure you are registered?\
                                        We cannot find this user.")
        return username

    def clean_password(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        try:
            user = User.objects.get(username=username)
        except:
            user = None
        if user is not None and not user.check_password(password):
            raise forms.ValidationError("Invalid password.")
        elif user is None:
            pass
        else:
            return password

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = User

"""from .models import *
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
            raise forms.ValidationError("Password should not all numeric")"""""
