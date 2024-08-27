from rest_framework import serializers
from .admin import User

class signUpserializers(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255, min_length=4)
    username = serializers.CharField(max_length=255, min_length=4)
    password = serializers.CharField(max_length=68, min_length=6, write_only=True)
    
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def validate(self, attrs):
        emailExist = User.objects.filter(email=attrs.get('email')).exists()
        if emailExist:
            raise serializers.ValidationError({'email': 'Email is already in use'})
        return super().validate(attrs)

