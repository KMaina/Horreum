import pytest
from horreum.apps.products.models import Product

@pytest.fixture(scope='function')
def create_product():
    product = Product.objects.create(name="Fish", quantity=30, UoM="KG", user_id=1)
    return product
