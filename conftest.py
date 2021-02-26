import pytest
import rest_framework

pytest_plugins = (
    "horreum.tests.fixtures.users",
    "horreum.tests.fixtures.products"
)

@pytest.fixture
def client():
    from rest_framework.test import APIClient
    return APIClient()
