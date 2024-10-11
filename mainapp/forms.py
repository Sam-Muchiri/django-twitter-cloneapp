from django.forms import ModelForm
from.models import Profiles,Blogs
from django import forms

class ProfileForm(ModelForm):
    class Meta:
        model=Profiles
        fields='__all__'
        exclude=['user']


class PostForm(forms.ModelForm):
    # post=forms.TextInput()
    class Meta:
        model=Blogs
        fields=['post']
        exclude=('user',)

class EditForm(forms.ModelForm):
    class Meta:
        model=Blogs
        fields=['post']