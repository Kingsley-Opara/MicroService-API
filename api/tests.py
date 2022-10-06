from django.test import TestCase
import requests
from getpass import getpass

# Create your tests here.

class TestApiRequest(TestCase):
    def test_create_user(self):
        endpoint = 'http://localhost:8000/token'
        username = 'udo@gmail.com'
        password = getpass()
        data = {
            'username': username,
            'password': password
        }
        res = requests.post(endpoint, json=data)
        self.assertEqual (res.status_code, 200)
    

    
