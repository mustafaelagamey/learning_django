from django import forms
from reviews.models import Feedback


class ReviewForm(forms.Form):
    user_name = forms.CharField(label='Enter Your name', required=True, max_length=100, error_messages={
        'required': 'Your name must not be empty',
        'max_length': 'Please enter a shorter name'
    })
    email = forms.EmailField()
    comment = forms.CharField()


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = '__all__'  # Selecting all fields
        # fields = ['user_name', 'comment']  # select some fields
        # exclude = ['excluded_field']  # exclude some fields
