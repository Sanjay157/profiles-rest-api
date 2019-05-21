from rest_framework import serializers
from . import models       #to define the class UserProfileSerializer


class HelloSerializer(serializers.Serializer):
    """Serializes a name field for tesing our APIView."""

    name = serializers.CharField(max_length=10)

class UserProfileSerializer(serializers.ModelSerializer):
    """Serializer for our user profile objects."""

    """We can define different field now as to name, email etc..But however we make use of ModelSerializer
         feature which is "Meta" class """
    class Meta:
        model = models.UserProfile   #This tells the Django rest framework that the ModelSerializer is going to be used with our UserProfile Model
        fields = ('id', 'email', 'name', 'password')
        extra_kwargs = {'password': {'write_only':True}}

    def create(self, validated_data):
        """Create and return a new user."""

        user = models.UserProfile(
            email = validated_data['email'],
            name = validated_data['name']
        )

        user.set_password(validated_data['password'])
        user.save()

        return user



