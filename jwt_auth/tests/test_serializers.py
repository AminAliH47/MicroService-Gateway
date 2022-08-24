from django.test import TestCase
from jwt_auth.serializers import UserLoginSerializer


class TestSerializers(TestCase):
    def test_user_serializer_valid_data(self):
        """
        Test User Login Serializer data is valid
        """
        serializer = UserLoginSerializer(
            data={
                "username": "test1",  # required
                "password": "Test12345",  # required
            }
        )

        self.assertTrue(serializer.is_valid())
