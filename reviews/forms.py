from django import forms


class ReviewForm(forms.Form):
    user_name = forms.CharField()
    email = forms.EmailField()
    comment = forms.CharField()

