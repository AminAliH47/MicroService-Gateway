from django.test import (
    TestCase,
    Client,
)
from django.urls import reverse


class TestViews(TestCase):
    def setUp(self):
        self.client = Client()

    def test_users_list_GET(self):
        """
        Test get users list successfully
        """
        response = self.client.get(reverse("crud:list"))

        self.assertEqual(response.status_code, 200)
