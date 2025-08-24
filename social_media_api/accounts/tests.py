from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model

User = get_user_model()

class AccountsAPITestCase(APITestCase):
    def setUp(self):
        # URLs for registration, login, and profile
        self.register_url = reverse('register')  # Make sure your urls.py name='register'
        self.login_url = reverse('login')        # Make sure your urls.py name='login'
        self.profile_url = reverse('profile')    # Make sure your urls.py name='profile'

        # Test user data
        self.user_data = {
            "username": "testuser",
            "email": "test@example.com",
            "password": "Testpass123!",
            "password2": "Testpass123!"
        }

    def test_user_registration(self):
        """Test that a user can register and receives a token"""
        response = self.client.post(self.register_url, self.user_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn('token', response.data)
        self.assertEqual(response.data['user']['username'], self.user_data['username'])

    def test_user_login(self):
        """Test that a registered user can log in and receive a token"""
        # First register the user
        self.client.post(self.register_url, self.user_data, format='json')

        # Prepare login data
        login_data = {
            "username": self.user_data['username'],
            "password": self.user_data['password']
        }
        response = self.client.post(self.login_url, login_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('token', response.data)
        self.assertEqual(response.data['username'], self.user_data['username'])

    def test_profile_retrieval_and_update(self):
        """Test that a logged-in user can view and update their profile"""
        # Register user
        register_response = self.client.post(self.register_url, self.user_data, format='json')
        self.assertEqual(register_response.status_code, status.HTTP_201_CREATED)
        token = register_response.data['token']

        # Authenticate the client
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {token}')

        # Retrieve profile
        response = self.client.get(self.profile_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['username'], self.user_data['username'])

        # Update profile
        update_data = {"bio": "I love Django REST Framework"}
        update_response = self.client.put(self.profile_url, update_data, format='json')
        self.assertEqual(update_response.status_code, status.HTTP_200_OK)
        self.assertEqual(update_response.data['bio'], update_data['bio'])
