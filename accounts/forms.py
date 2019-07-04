from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control'}
    ))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control'}
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
    email = forms.EmailField(label='Email')
    password = forms.CharField(label='Password', widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Password'}
    ))
    passwordconf = forms.CharField(label='Password confirmation ', widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Password confirmation'}
    ))
    class Meta:
        model = User
        fields = ['username', 'email']

    def clean_passwordconf(self):
        password = self.cleaned_data.get("password")
        passwordconf = self.cleaned_data.get("passwordconf")
        if password and passwordconf and password != passwordconf:
            raise forms.ValidationError("Passwords do not match")
        return passwordconf

    def clean_email(self):
        email = self.cleaned_data.get("email")
        user_count = User.objects.filter(email=email).count()
        if user_count > 0:
            raise forms.ValidationError("This email has already been\
                                     registered. Please reset your password.")
        return email

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user

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
