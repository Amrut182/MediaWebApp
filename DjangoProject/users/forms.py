from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserLoginForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)
        email = forms.EmailField()
        self.fields['email'].required = True
        self.fields['password1'].widget = forms.PasswordInput(attrs={'placeholder': 'Password', 'class': 'input100'})
        self.fields['password2'].widget = forms.PasswordInput(attrs={'placeholder': 'Re-Enter Password', 'class': 'input100'})
    class Meta:
        model = User
        fields = ['username','email','password1','password2']
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Username' ,'class':'input100'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email' , 'class':'input100'}),
            'password1': forms.PasswordInput(attrs={ 'class':'input100' , 'type' : 'password'}),
            'password2': forms.PasswordInput(attrs={'placeholder': 'password2', 'class':'input100' , 'type' : 'password'}),
        }   
