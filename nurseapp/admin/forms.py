from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(label="Usuario", required=True, max_length=25)
    password = forms.CharField(widget=forms.PasswordInput)
