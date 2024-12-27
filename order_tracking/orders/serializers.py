from rest_framework import serializers
from .models import Customer, Product, Order

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id', 'name', 'email']


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'price']


class OrderSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer()
    product = ProductSerializer()

    class Meta:
        model = Order
        fields = ['id', 'customer', 'product', 'quantity', 'order_date', 'status']

    def create(self, validated_data):
        # Extraire les données imbriquées pour customer et product
        customer_data = validated_data.pop('customer')
        product_data = validated_data.pop('product')

        # Créer ou récupérer l'objet Customer
        customer, created = Customer.objects.get_or_create(**customer_data)

        # Créer ou récupérer l'objet Product
        product, created = Product.objects.get_or_create(**product_data)

        # Créer la commande avec le customer et product
        order = Order.objects.create(customer=customer, product=product, **validated_data)

        return order


