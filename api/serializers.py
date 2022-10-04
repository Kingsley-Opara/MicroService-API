from rest_framework import serializers
from django.contrib.auth import get_user_model
from .validators import validate_email, validate_username

User = get_user_model()

class UserSerializers(serializers.ModelSerializer):
    # created = serializers.SerializerMethodField(read_only = True)
    # unique_id = serializers.SerializerMethodField(read_only = True)
    email = serializers.EmailField(validators = [validate_email])
    username = serializers.CharField(validators = [validate_username])

    class Meta:
        model = User
        fields = ['email', 'username', 'password']

