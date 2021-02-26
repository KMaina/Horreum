import enum

from rest_framework import serializers
from .models import Product, User


class UserRelatedField(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name')

    def get_queryset(self):
        user = self.context['request'].user
        queryset = User.objects.filter(id=user.id)
        if not queryset or not user:
            return None
        return queryset

class ProductSerializer(serializers.ModelSerializer):
    class Units(enum.Enum):
        """Different units of measurements"""
        NONE = "NONE", "none"
        KG = "KG", "kg"
        L = "L", "l"
        PACKETS = "PACKETS", "packets"


    name = serializers.CharField(max_length=100)
    quantity = serializers.IntegerField(default=0)
    unit = [unit.value for unit in Units]
    UoM = serializers.ChoiceField(choices=unit, required=True)
    user = UserRelatedField(read_only=True)

    class Meta:
        model = Product
        fields = ['name', 'quantity', 'UoM', 'user']

    def create(self, validated_data):
        return Product.objects.create(name=validated_data['name'], quantity=validated_data['quantity'], UoM=validated_data['UoM'], user=self.context['request'].user)
