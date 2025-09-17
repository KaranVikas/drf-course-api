from rest_framework import serializers
from .models import Product, Order, OrderItem

class ProductSerializer(serializers.ModelSerializer):
  class Meta:
    model = Product
    fields = (
      'name',
      'description',
      'price',
      'stock',
    )

  # valdiation function on the serializer
  def validate_price(self, value):
    if value <= 0:
      raise serializers.ValidationError(
        "prices must be greater than zero"
      )
    return value


class OrderSerializer(serializers.Serializer):
  class Meta:
    model: Order
    fields = (

    )

