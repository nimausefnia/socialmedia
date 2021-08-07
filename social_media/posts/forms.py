from django import forms
from django.shortcuts import get_object_or_404
from posts.models import Comment, Post

class AddPostForm(forms.ModelForm):
    class Meta:
        model=Post 
        fields=('body',)



class EditPostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=('body',)
        

class AddCommentForm(forms.ModelForm):
     class Meta:
         model=Comment
         fields=('body',)
         widgets={
             'body':forms.Textarea(attrs={'class':"form-control"})
         }
         help_text={
             'body':'max 400 length'
         }

    
class AddReplyForm(forms.ModelForm):

    class Meta:
        model=Comment
        fields=('body',)
        