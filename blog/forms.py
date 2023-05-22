from django import forms
from django.forms import TextInput, NumberInput, Textarea

from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ['post']
        widgets = {
            'user_name': forms.TextInput(
                attrs={'placeholder': 'Name',
                       'style': 'width: 70%;',
                       'class': 'form-control form-group'}),
            'user_email': forms.TextInput(
                attrs={'placeholder': 'example@example.com',
                       'style': 'width: 70%;',
                       'class': 'form-control form-group'}),
            'text': Textarea(
                attrs={'placeholder': 'Rating',
                       'style': "width:70%; height: 6rem;",
                       'class': "form-control form-group"})
        }
        labels = {
            'user_name': 'Your Name',
            'user_email': 'Your Email',
            'text': "Comment"
        }
