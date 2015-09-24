from django import forms
from django.contrib.auth.models import User
from fotalkapp.models import *
from django.contrib.auth import login, authenticate
import requests

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['text', 'country_code']
        exclude = ('user',)

    def clean(self):
        cleaned_data = super(PostForm, self).clean()
        return cleaned_data

class RegisterForm(forms.ModelForm):
    password_confirm = forms.CharField(max_length = 200, widget = forms.PasswordInput())
    first_name = forms.CharField(max_length=40, required=True)
    last_name = forms.CharField(max_length=40, required=True)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'password']
        widgets = { 'password': forms.PasswordInput(), } 

    def clean(self):
        # Calls our parent (forms.Form) .clean function, gets a dictionary
        # of cleaned data as a result
        cleaned_data = super(RegisterForm, self).clean()

        # Confirms that the two password fields match
        password1 = cleaned_data.get('password')
        password2 = cleaned_data.get('password_confirm')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords do not match.")

        # Generally return the cleaned data we got from our parent.
        return cleaned_data

    # Customizes form validation for the username field.
    def clean_username(self):
        # Confirms that the username is not already present in the
        # User model database.
        username = self.cleaned_data.get('username')
        if User.objects.filter(username__exact=username):
            raise forms.ValidationError("Username is taken.")

        # Generally return the cleaned data we got from the cleaned_data
        # dictionary
        return username