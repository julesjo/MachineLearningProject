from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.forms.fields import FileField
from django.forms import ModelForm
from .models import AudioFile

class register(forms.Form):
    FirstName = forms.CharField(label="First Name",max_length=200)
    LastName = forms.CharField(label="Last Name",max_length=200)
    Email = forms.EmailField(label="Email ID",max_length=200)
    Password=forms.CharField(label="Password",widget=forms.PasswordInput(),max_length=32)
    ConfirmPassword=forms.CharField(label="Confirm Password",widget=forms.PasswordInput(),max_length=32)

class talknow(forms.Form):
    Audio = forms.FileField(label="Talk Now")
    AudioTranscribed = forms.Textarea()
