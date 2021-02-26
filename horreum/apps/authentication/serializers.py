import enum

from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from rest_framework_simplejwt.tokens import RefreshToken, TokenError

from .models import User, Accountant, Cashier, StoreKeeper, Supervisor, Attendant

class UserRegistrationSerializer(serializers.ModelSerializer):
    class Roles(enum.Enum):
        """Different roles for the user types"""
        ATTENDANT = "ATTENDANT", "Attendant"
        CASHIER = "CASHIER", "Cashier"
        STORE_KEEPER = "STORE_KEEPER", "Store_keeper"
        ACCOUNTANT = "ACCOUNTANT", "Accountant"
        SUPERVISOR = "SUPERVISOR", "Supervisor"

    password = serializers.CharField(min_length=4, max_length=100)
    roles = [role.value for role in Roles]
    role = serializers.ChoiceField(choices=roles, required=True)
    first_name = serializers.CharField(max_length=100)
    last_name = serializers.CharField(max_length=100)
    username = serializers.CharField(max_length=100, required=True, validators=[UniqueValidator(queryset=User.objects.all())])
    email = serializers.CharField(max_length=100, required=True, validators=[UniqueValidator(queryset=User.objects.all())])

    class Meta:
        model = User
        fields = ['first_name', 'username','email', 'password','role', 'first_name', 'last_name']

        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        role = self.validated_data['role']
        if role == 'ACCOUNTANT':
            user = Accountant.objects.create(
                username=validated_data['username'],
                email=validated_data['email'],
                first_name=validated_data['first_name'],
                last_name=validated_data['last_name'],
                password=validated_data['password'],
                role=role
                )

        elif role == 'CASHIER':
            user = Cashier.objects.create(
                username=validated_data['username'],
                email=validated_data['email'],
                first_name=validated_data['first_name'],
                last_name=validated_data['last_name'],
                password=validated_data['password'],
                role=role
                )

        elif role == 'STORE_KEEPER':
            user = StoreKeeper.objects.create(
                username=validated_data['username'],
                email=validated_data['email'],
                first_name=validated_data['first_name'],
                last_name=validated_data['last_name'],
                password=validated_data['password'],
                role=role
                )
        
        elif role == 'ATTENDANT':
            user = Attendant.objects.create(
                username=validated_data['username'],
                email=validated_data['email'],
                first_name=validated_data['first_name'],
                last_name=validated_data['last_name'],
                password=validated_data['password'],
                role=role
                )
        
        elif role == 'SUPERVISOR':
            user = Supervisor.objects.create(
                username=validated_data['username'],
                email=validated_data['email'],
                first_name=validated_data['first_name'],
                last_name=validated_data['last_name'],
                password=validated_data['password'],
                role=role
                )

        return user
