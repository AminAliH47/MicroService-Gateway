from django.test import TestCase
from django.urls import (
    reverse,
    resolve,
)
from crud import views


class TestUrls(TestCase):
    def test_list_url_is_resolved(self):
        """
        Test List URL is resolved in crud app
        """
        url = reverse("crud:list")
        self.assertEqual(resolve(url).func.view_class, views.UsersList)

    def test_retrieve_url_is_resolved(self):
        """
        Test Retrieve URL is resolved in crud app
        """
        url = reverse("crud:retrieve", kwargs={"pk": 1})
        self.assertEqual(resolve(url).func.view_class, views.RetrieveUser)

    def test_create_url_is_resolved(self):
        """
        Test Create URL is resolved in crud app
        """
        url = reverse("crud:create")
        self.assertEqual(resolve(url).func.view_class, views.CreateUser)

    def test_update_url_is_resolved(self):
        """
        Test Update URL is resolved in crud app
        """
        url = reverse("crud:update", kwargs={"pk": 1})
        self.assertEqual(resolve(url).func.view_class, views.UpdateUser)

    def test_delete_url_is_resolved(self):
        """
        Test Delete URL is resolved in crud app
        """
        url = reverse("crud:delete", kwargs={"pk": 1})
        self.assertEqual(resolve(url).func.view_class, views.DeleteUser)
