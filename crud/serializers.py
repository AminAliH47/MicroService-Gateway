from rest_framework import serializers


class UserSerializer(serializers.Serializer):
    """
    User serializer to validate user data
    """
    id = serializers.IntegerField(required=False)
    username = serializers.CharField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField()
