from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm

class signupForm(UserCreationForm):
    email=forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}), error_messages={'required':'enter your email boss'})
    password1=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'confirm password'}))
    
    class Meta:
        model=User
        fields=['username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(signupForm, self).__init__( *args, **kwargs)
        self.fields['username'].widget.attrs['class']='field'
        self.fields['username'].help_text=''
        self.fields['email'].help_text=''
        self.fields['password1'].help_text=''
        # self.fields['password1'].widget.attrs['class']='field'
        self.fields['password2'].help_text=''

    