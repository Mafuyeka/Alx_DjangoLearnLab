# blog/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post, Comment, Profile

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title','content','tags']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ['username','email']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio','photo']
