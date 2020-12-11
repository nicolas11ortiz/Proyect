from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from . models import  Juego
from django import forms

class JuegoForm(ModelForm):
    class Meta:
        model = Juego
        fields = '__all__'

class createUserForm(UserCreationForm):
    error_messages = {
            'password_mismatch': '¡Las contraseñas no coinciden!'
        }
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={
                'placeholder':'Nombre de usuario',
            }), 
            'email': forms.EmailInput(attrs={
                'placeholder':'Correo@MiCorreo.com',
            })
        }
        error_messages = {
            'username': {
                'unique': '¡El nombre de usuario ya existe!',
            }
        }