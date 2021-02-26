import json, pytest
from django.urls import reverse
from rest_framework import status

class TestCrudAuthentication:
    """Test Cases for the User CRUD"""
    @pytest.mark.django_db
    def test_admin_can_create_attendants(self, client, admin, get_or_create_admin_token):
        """Test that an admin can create a new attendant"""
        new_attendant = {
                "username": "new_attendant",
                "email": "new_attendant@me.com",
                "password": "1234",
                "first_name": "Att",
                "last_name": "Att",
                "name": "att",
                "role": "ATTENDANT"
            }
        token = get_or_create_admin_token
        url = reverse('authentication:registration')
        client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)
        response = client.post(url, new_attendant)
        assert response.status_code == status.HTTP_201_CREATED

    @pytest.mark.django_db
    def test_admin_can_create_store_keepers(self, client, admin, get_or_create_admin_token):
        """Test that an admin can create a new store keepers"""
        new_store_keeper = {
                "username": "new_store_keeper",
                "email": "new_store_keeper@me.com",
                "password": "1234",
                "first_name": "Store",
                "last_name": "Keeper",
                "name": "keeper",
                "role": "STORE_KEEPER"
            }
        token = get_or_create_admin_token
        url = reverse('authentication:registration')
        client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)
        response = client.post(url, new_store_keeper)
        assert response.status_code == status.HTTP_201_CREATED

    @pytest.mark.django_db
    def test_admin_can_create_accountants(self, client, admin, get_or_create_admin_token):
        """Test that an admin can create a new accountant"""
        new_accountant = {
                "username": "new_accountant",
                "email": "new_accountant@me.com",
                "password": "1234",
                "first_name": "Accountant",
                "last_name": "Accountant",
                "name": "keeper",
                "role": "ACCOUNTANT"
            }
        token = get_or_create_admin_token
        url = reverse('authentication:registration')
        client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)
        response = client.post(url, new_accountant)
        assert response.status_code == status.HTTP_201_CREATED

    @pytest.mark.django_db
    def test_admin_can_create_cashier(self, client, admin, get_or_create_admin_token):
        """Test that an admin can create a new cashier"""
        new_cashier = {
                "username": "new_cashier",
                "email": "new_cashier@me.com",
                "password": "1234",
                "first_name": "Cashier",
                "last_name": "Cashier",
                "name": "keeper",
                "role": "CASHIER"
            }
        token = get_or_create_admin_token
        url = reverse('authentication:registration')
        client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)
        response = client.post(url, new_cashier)
        assert response.status_code == status.HTTP_201_CREATED