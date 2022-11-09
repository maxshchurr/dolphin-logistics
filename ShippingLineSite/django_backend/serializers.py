from rest_framework import serializers
from .models import Order, Company


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

    def create(self, validated_data):
        return Order.objects.create(validated_data)

    def update(self, instance, validated_data):
        instance.departure_location = validated_data.get('departure_location', instance.departure_location)
        instance.delivery_location = validated_data.get('delivery_location', instance.delivery_location)
        instance.container_type = validated_data.get('container_type', instance.container_type)
        instance.container_weight = validated_data.get('container_weight', instance.container_weight)


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'

    def create(self, validated_data):
        return Company.objects.create(validated_data)

    def update(self, instance, validated_data):
        instance.company_name = validated_data.get('company_name', instance.company_name)
        instance.company_location = validated_data.get('company_location', instance.company_location)