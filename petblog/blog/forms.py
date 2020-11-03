from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={'rows':1,
                                'placeholder':'Add your comment...'}), label='')
    class Meta:
        model = Comment
        fields = ['content']