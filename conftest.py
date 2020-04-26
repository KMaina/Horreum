import pytest
import rest_framework


@pytest.fixture
def api_client():
    from rest_framework.test import APIClient
    return APIClient()
