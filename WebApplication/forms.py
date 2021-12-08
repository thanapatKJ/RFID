from django import forms
from django.forms import Textarea, TextInput, ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms.widgets import Select, DateTimeInput


from .models import ObjectInfo

class UserForm(UserCreationForm):
    class Meta:
        model=User
        fields=('username','first_name','last_name','email','password1','password2')
        widgets = {
            'username': TextInput(attrs = {
                'class': 'form-group w-50'
            }),
            'first_name': TextInput(attrs = {
                'class': 'form-group w-50'
            }),
            'email': TextInput(attrs = {
                'class': 'form-group w-50'
            }),
            'password1': TextInput(attrs = {
                'class': 'form-group w-50'
            }),
            'password2': TextInput(attrs = {
                'class': 'form-group w-50'
            }),
            'last_name': TextInput(attrs = {
                'class': 'form-group w-50'
            }),
        }

class ObjectForm(ModelForm):
    class Meta:
        all_status = [
        ('อุปกรณ์อยู่','อุปกรณ์อยู่'), 
        ('อุปกรณ์ไม่อยู่','อุปกรณ์ไม่อยู่'),
        ]
        model = ObjectInfo
        fields = ('tag_id','tag_name','picture')
        widgets = {
            'tag_id': TextInput(attrs = {
                'class': 'form-group w-50'
            }),
            'tag_name': TextInput(attrs = {
                'class': 'form-group w-50'
            }),
        }