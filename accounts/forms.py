from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()

class AdminChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ['email', 'username', 'password']

    
    def clean_password(self):
        return self.initial['password']

