from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()

def validate_email(value):
    email = User.objects.filter(email__iexact = value)
    if email.exists():
        raise serializers.ValidationError('Invalid email')
    return value

def validate_username(value):
    email = User.objects.filter(username__iexact = value)
    if email.exists():
        raise serializers.ValidationError('Invalid username and password')
    return value