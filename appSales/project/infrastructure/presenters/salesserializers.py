from rest_framework import serializers
from entities.sales.salesmodels import Sale

class SaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sale
        fields = '__all__'