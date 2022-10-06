from django.urls import path
from django.views.generic import TemplateView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('', TemplateView.as_view(template_name = 'home.html'), name='home'),
    path('token/', obtain_auth_token)
]