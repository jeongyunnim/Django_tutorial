from django import forms
from django.forms import ModelForm
from .models import Review

# class ReviewForm(forms.Form):
#     first_name = forms.CharField(label='first_name', max_length=100)
#     last_name = forms.CharField(label='last_name', max_length=100)
#     email = forms.EmailField(label='Email')
#     review = forms.CharField(label='Please write your review here',
#                              widget=forms.Textarea(attrs={'class':'myform'}))

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = "__all__"
        # fields = ['first_name', 'last_name', 'stars']
        labels = {
            'first_name':"Your First Name",
            'last_name':"Your Last Name",
            'stars':'Rating',
        }

        error_messages = {
            'stars':{
                'min_value':'최솟값은 1이라네',
                'max_value':'최댓값은 5라네'
            }
        }