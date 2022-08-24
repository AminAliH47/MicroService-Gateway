from django.test import TestCase
from django.urls import (
    reverse,
    resolve,
)
from rest_framework_simplejwt.views import TokenRefreshView
from jwt_auth import views


class TestUrls(TestCase):
    def test_list_url_is_resolved(self):
        """
        Test Login URL is resolved in jwt_auth app
        """
        url = reverse("jwt_auth:login")

        self.assertEqual(resolve(url).func.view_class, views.LoginView)

    def test_get_refresh_token_url_is_resolved(self):
        """
        Test Get Refresh Token URL is resolved in jwt_auth app
        """
        url = reverse("jwt_auth:token_refresh")

        self.assertEqual(resolve(url).func.view_class, TokenRefreshView)
