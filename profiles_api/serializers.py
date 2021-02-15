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
