from datetime import datetime

from django import forms
from django.contrib.auth import get_user_model

from main.models import Recipe, Image, Comment


class RecipeForm(forms.ModelForm):
    created = forms.DateTimeField(
        initial=datetime.now().strftime('%Y-%m-%d'),
        required=False
    )

    class Meta:
        model = Recipe
        fields = '__all__'


class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('image', )


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text', )


class UserRegistrationForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ('email', 'password', 'username')


class AuthorizationForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(max_length=100)
