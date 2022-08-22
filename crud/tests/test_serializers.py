from django.test import TestCase

from crud.serializers import UserSerializer


class TestSerializers(TestCase):
    def test_user_serializer_valid_data(self):
        """
        Test User Proto Serializer data is valid
        """
        serializer = UserSerializer(
            data={
                "username": "test1",  # required
                "first_name": "First test1",
                "last_name": "Last test1",
                "email": "test1@test.com",
                "password": "Test12345",  # required
            }
        )

        self.assertTrue(serializer.is_valid())

    def test_user_serializer_empty_data(self):
        """
        Test User Proto Serializer with empty data is invalid
        """
        serializer = UserSerializer(data={})

        self.assertFalse(serializer.is_valid())
        self.assertEqual(len(serializer.errors), 2)
