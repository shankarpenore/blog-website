from django import forms
from . import models
class PostCreationForm(forms.ModelForm):
    # author = forms.CharField()
    class Meta:
        model = models.Post
        fields = ['title', 'content']

class PostEditForm(forms.ModelForm):
    class Meta :
        model = models.Post
        fields = ['title', 'content']

class CommentCreationForm(forms.ModelForm):

    class Meta:
        model = models.Comment
        fields = ['comment']

class CommentEditForm(forms.ModelForm):

    class Meta:
        model = models.Comment
        fields = ['comment']