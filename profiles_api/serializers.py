from rest_framework import serializers
from profiles_api import models

class HelloSerializer(serializers.Serializer):
    """Serializes a name fields for testing our APIView"""
    name = serializers.CharField(max_length = 10)

class UserProfileSerializer(serializers.ModelSerializer):                       # A model serializer.
    """Serializes a user profile object"""

    class Meta:                                                                 # A meta class.
        model = models.UserProfile                                              # This sets our serializer up to point to our UserProfile model.
        fields = ('id', 'email', 'name', 'password')                            # Specify the list of fields in our model that we want to manage through our serializer.
                                                                                # So this is a list of all the fields that you want to either make accessible in our API or you want to
                                                                                # either make accessible in our API or you want to use to create new models with our serializer.
        extra_kwargs = {                                                        # We want to make an exception for password field because of security reasons.
            'password' : {
                'write_only' : True,                                            # Sets up for write only.
                'style' : {'input_type' : 'password'}                           # This makes the text visible only as "*" or dots in password text box - only for browsable API.
            }
        }

    def create(self, validated_data):                                           # We have to overwrite the create function. By default the model serializer allows you to create simple
                                                                                # objects in the databese. So it uses the default create function of the object manager to create the object.
                                                                                # We want to override this functionality for this particular serializer so that it uses the create user function.
                                                                                # The reason we do this is so that the password gets created as a hash and not the clear text password that it would
                                                                                # do by default if we did not override the function.
        """Create and return a new user"""
        user = models.UserProfile.objects.create_user(                          # Create a new user with email, name and password arguments
            email = validated_data['email'],
            name = validated_data['name'],
            password = validated_data['password']
        )

        return user

    def update(self, instance, validated_data):                                 # The default update logic for the Django REST Framework (DRF) ModelSerializer code will take whatever
                                                                                # fields are provided (in our case: email, name, password) and pass them directly to the model.
                                                                                # This is fine for the email and name fields, however the password field requires some additional logic
                                                                                # to hash the password before saving the update.
        """Handle updating user account"""
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)

        return super().update(instance, validated_data)


class ProfileFeedItemSerializer(serializers.ModelSerializer):
    """Serializes profile feed items"""

    class Meta:
        model = models.ProfileFeedItem                                          # ProfileFeedItem has 3 fields (check models.py) - we need to make these fields available through serializer
                                                                                # in next lines.
        fields = ('id', 'user_profile', 'status_text', 'created_on')            # Include the ID so we can use that to retrieve specific objects and by default Django adds a primary key
                                                                                # ID to all models that you create. Because the ID is set up by Django by default it is automatically set
                                                                                # to read only. The created_on is automatically set to the time that it is created so that will by default
                                                                                # be read-only.

        extra_kwargs = {                                                        # We do not want the users to be able to set the user_profile when they create a new feed item. We want
            'user_profile' : {'read_only' : True}                               # to set the user_profile based on the user that is authenticated. That is why we set user_profile to read-only.
        }
