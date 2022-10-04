from django.urls import path
from .views import CreateUserApi

urlpatterns = [
    path('create/', CreateUserApi.as_view(), name='create_api')
]
