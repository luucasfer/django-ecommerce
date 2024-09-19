from django.contrib.auth.forms import UserCreationForm
from userauths.models import User
from django import forms


class UserRegisterForm(UserCreationForm):
    # cria um atributo dentro do form do username 
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirm your password'}))

    # utiliza o meu modelo no UserCreationForm
    class Meta:
        model = User
        fields = ['username', 'email']
