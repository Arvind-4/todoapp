from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()


class SignUpForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirm password", widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data.get("username")
        qs = User.objects.filter(username__iexact=username)
        if qs.exists():
            msg = "Username is taken. Please try another one."
            raise forms.ValidationError(msg)
        return username

    def clean_password2(self):
        password = self.cleaned_data.get("password")
        password2 = self.cleaned_data.get("password2")
        if password2 != password:
            msg = "Passwords must match. Please try again."
            raise forms.ValidationError(msg)
        return password2
