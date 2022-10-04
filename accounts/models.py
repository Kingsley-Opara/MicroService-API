from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
import secrets
import random
from django.db.models.signals import pre_save, post_save
from django.template.loader import render_to_string
from django.conf import settings
from django.core.mail import send_mail
import pathlib
BASE_DIR = pathlib.Path(__file__).resolve().parent


# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, email, password, **other_fields):
        if not email:
            raise ValueError('All users must have an email')
        
        email = self.normalize_email(email)
        user = self.model(email=email, password=password, **other_fields)
        user.set_password(password)
        user.save()

        return user
    
    def create_staffuser(self, email, password, **other_fields):
        other_fields.setdefault('is_active', True)
        other_fields.setdefault('is_staff', True)

        if not other_fields.get('is_active'):
            raise ValueError('Staff users must have an active accounts')
        
        user = self.create_user(
            email=email,
            password=password,
            **other_fields
        )

        return user
    def create_superuser(self, email, password, **other_fields):
        other_fields.setdefault('is_active', True)
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)

        if not other_fields.get('is_active'):
            raise ValueError('Staff users must have an active accounts')
        if not other_fields.get('is_staff'):
            raise ValueError('Admin users must have a staff account')
        
        user = self.create_user(
            email=email,
            password=password,
            **other_fields
        )

        return user




class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True, verbose_name = 'Email')
    unique_id = models.CharField(default= f'{secrets.token_urlsafe(6)}{random.randint(0, 9)}', max_length=15, 
    editable=False, unique=True, null=True, blank=True)
    username = models.CharField(max_length=35, null=True, blank=True, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    REQUIRED_FIELDS = ['email']
    USERNAME_FIELD = 'username'
    objects = UserManager()

    def __str__(self):
        return self.email

def save_method(instance, save=False):
    if save:
        instance.save()

def post_save_signal(sender, instance, created, *args, **kwargs):
    subject = 'Welcome to DataSTACK'
    html_template = str(f'{BASE_DIR}/templates/email_sent.html')
    message = render_to_string(html_template, {'uid': instance.unique_id})
    if created:
        instance.username = instance.email
        if not instance.email: 
            instance.email = instance.username

        send_mail(subject, '', '', [instance.email], fail_silently=False, html_message=message)
    
        save_method(instance, save=True)

post_save.connect(post_save_signal, sender=User)