from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from django.contrib.auth import get_user_model
from .permissions import UserPermission
from .serializers import UserSerializers
from rest_framework import authentication
from .authentication import TokenAuthentication

User = get_user_model()
# Create your views here.

class CreateUserApi(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializers 
    permission_classes = [UserPermission]
    authentication_classes = [authentication.SessionAuthentication, TokenAuthentication]
