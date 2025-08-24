from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model

User = get_user_model()


class AccountsAPITestCase(APITestCase):
    def setUp(self):
        self.register_url = reverse("register")
        self.login_url = reverse("login")
        self.profile_url = reverse("profile")
        self.user_data = {
            "username": "testuser",
            "email": "testuser@example.com",
            "password": "testpass123",
        }

    def test_user_registration(self):
        """Test that a user can register and receives a token"""
        response = self.client.post(self.register_url, self.user_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("token", response.data)
        self.assertIn("user", response.data)
        self.assertEqual(response.data["user"]["username"], self.user_data["username"])

    def test_user_login(self):
        """Test that a registered user can log in and receive a token"""
        # First register user
        self.client.post(self.register_url, self.user_data, format="json")
        # Then login
        response = self.client.post(
            self.login_url,
            {
                "username": self.user_data["username"],
                "password": self.user_data["password"],
            },
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("token", response.data)
        self.assertEqual(response.data["username"], self.user_data["username"])

    def test_profile_retrieval_and_update(self):
        """Test that a logged-in user can view and update their profile"""
        # Register user
        register_response = self.client.post(self.register_url, self.user_data, format="json")
        token = register_response.data["token"]

        # Authenticate client once for all future requests
        self.client.credentials(HTTP_AUTHORIZATION="Token " + token)

        # Retrieve profile
        response = self.client.get(self.profile_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["username"], self.user_data["username"])

        # Update profile
        update_response = self.client.put(
            self.profile_url,
            {"bio": "I love Django REST Framework"},
            format="json",
        )
        self.assertEqual(update_response.status_code, status.HTTP_200_OK)
        self.assertEqual(update_response.data["bio"], "I love Django REST Framework")
