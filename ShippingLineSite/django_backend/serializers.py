from rest_framework import serializers
from rest_framework.authtoken.views import Token
from .models import Order, Company, SalesManager
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password']

        # Special features for password field
        extra_kwargs = {'password': {
            'write_only': True,
            'required': True
        }}

    # User creation and token generation
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'


class SalesManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalesManager
        fields = '__all__'
