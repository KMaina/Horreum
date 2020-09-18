from rest_framework import serializers

from models import User


def password_validate():
    return serializers.RegexField(
        regex='^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[@#$%^&+=*!])',
        max_length=128,
        min_length=8,
        write_only=True,
        error_messages={
            'required': 'Password field required',
            'min_length': 'Ensure Password field has at least 8 characters',
            'invalid': 'Password should contain a lowercase, uppercase numeric'
            ' and special character'
        })


class RegisterSerializer(serializers.ModelSerializer):
    password = password_validate()
    confirm_password = password_validate()

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
