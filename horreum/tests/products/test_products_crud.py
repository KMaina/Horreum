import pytest, json
from django.urls import reverse
from rest_framework import status


class TestProductCrud:
    @pytest.mark.django_db
    def test_create_product(self, client, get_or_create_admin_token):
        product = {
            "name": "Fish",
            "quantity": 30,
            "UoM": "KG"
        }
        token = get_or_create_admin_token
        client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)
        url = reverse('products:product-list')
        response = client.post(url, product)
        assert response.status_code == status.HTTP_201_CREATED
