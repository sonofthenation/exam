from django import forms
from .models import CustomUser


class RegistrationForm(forms.ModelForm):
    confirm_password=forms.CharField()
    class Meta:
        model=CustomUser
        fields=[
            'username',
            'email',
            'password',
        ]
    def clean_email(self):
        data=self.cleaned_data
        email=data['email']
        email_list=CustomUser.objects.values_list('email',flat=True)
        if email in email_list:
            raise forms.ValidationError("This email is already registered, try to log in")
        return email

    def clean_password(self):
        data=self.cleaned_data
        password=data['password']
        confirm_password=data['confirm_password']
        if confirm_password==password:
            return password
        raise forms.ValidationError("Password doesn't match")

    def save(self, commit=True):
        data=self.cleaned_data
        username=data['username']
        email=data['email']
        password=data['password']
        user=CustomUser.objects.create_user(username=username,email=email,password=password)
        return user

class LoginForm(forms.Form):
    username_or_email=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput)

    def is_email(self):
        data=self.cleaned_data
        username_or_email=data['username_or_email']
        if len(username_or_email.split('@'))>1:
            return True
        return False



