from rest_framework import serializers
from .models import Order, OrderItem, Customer, Merchant


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ("product", "quantity")


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ("name",)


class MerchantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Merchant
        fields = ("name",)


class OrderSerializer(serializers.ModelSerializer):
    order_items = OrderItemSerializer(source="orderitem_set", many=True)
    customer = CustomerSerializer()
    merchant = MerchantSerializer()

    class Meta:
        model = Order
        fields = ("customer", "merchant", "order_date", "order_items")
