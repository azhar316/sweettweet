from django import forms

from .models import Tweet, TweetComment


class TweetForm(forms.ModelForm):

    class Meta:
        model = Tweet
        fields = ['text', 'media']
        widgets = {
            'text': forms.Textarea(attrs={'cols': 50, 'rows': 5})
        }


class TweetCommentForm(forms.ModelForm):

    class Meta:
        model = TweetComment
        fields = ['text']
        widgets = {
            'text': forms.Textarea(attrs={'cols': 50, 'rows': 2})
        }

