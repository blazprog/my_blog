from django import forms
from .models import Post, Comment

from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text',)
        widgets = {
            'title': forms.TextInput(attrs={'class': 'input is-medium blog-title'}),
            'text': SummernoteWidget(attrs={'class': 'textarea'}),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('comment', )
        widgets = {
            'comment': SummernoteWidget(attrs={'class': 'textarea'}),
        }


# class CommentForm(forms.ModelForm):
#     class Meta:
#         model = Comment
#         fields = ('body', )
#         widgets = {
#             'body': forms.Textarea(attrs={'class': 'textarea', 'rows':3,
#                                           'placeholder': 'Добавить коментар'}),
#         }
