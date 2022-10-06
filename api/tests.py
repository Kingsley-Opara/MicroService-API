from django.test import TestCase
import requests
from getpass import getpass
from django.contrib.auth import get_user_model
# Create your tests here.
User = get_user_model()

class TestApiRequest(TestCase):
    def setup(self):
        users = User.objects.all()

    def test_create_user(self):
        endpoint = 'http://localhost:8000/token/'
        user_input = input('Enter your username: ')
        username = user_input
        password = getpass()
        data = {
            'username': username,
            'password': password
        }
        res = requests.post(endpoint, json=data)
        self.assertEqual (res.status_code, 200)
    

    
