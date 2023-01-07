from django import forms
from .models import Feed

class FeedForm(forms.ModelForm):
    class Meta:
        model = Feed
        fields = ['user','content']
    
        labels = {
            'user' : "사용자",
            'content' : "내용"
        }
        
    