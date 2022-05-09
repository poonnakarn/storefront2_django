from decimal import Decimal
from gc import collect
from pyexpat import model
from rest_framework import serializers

from store.models import Product, Collection


class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = ['id', 'title', 'products_count']

    products_count = serializers.IntegerField()

    # products_count = serializers.SerializerMethodField(
    #     method_name='calculate_products_count')

    # def calculate_products_count(self, collection: Collection):
    #     return Product.objects.filter(collection=collection).count()


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title', 'description', 'slug', 'inventory',
                  'unit_price', 'price_with_tax', 'collection']
    price_with_tax = serializers.SerializerMethodField(
        method_name='calculate_tax')

    def calculate_tax(self, product: Product):
        return product.unit_price * Decimal(1.1)
