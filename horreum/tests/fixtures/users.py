import pytest, json
from django.urls import reverse
from horreum.apps.authentication.models import User, Accountant, Attendant, Cashier, StoreKeeper, Supervisor

@pytest.fixture(scope='function')
def admin():
    admin = User.objects.create_superuser(
                email='admin@me.com',
                username='admin',
                password='1234',
                first_name='Admin',
                last_name='Admin')
    return admin

@pytest.fixture
def get_or_create_admin_token(db, client, admin):
    admin.save()
    url = reverse('authentication:token_obtain_pair')
    my_data =  {
        "email": "admin@me.com",
        "password": "1234"
	}
    response = client.post(url,data=json.dumps(my_data),
                                   content_type='application/json')
    token =  response.data['access']
    return token

@pytest.fixture(scope='function')
def cashier1():
    cashier1 = Cashier.objects.create(
                email='cashier1@me.com',
                username='cashier1',
                password='1234',
                first_name='Cashier1',
                last_name='Cashier1')
    return cashier1

@pytest.fixture
def get_or_create_cashier_token(db, client, cashier1):
    cashier1.save()
    url = reverse('authentication:token_obtain_pair')
    my_data =  {
        "email": "cashier1@me.com",
        "password": "1234"
	}
    response = client.post(url,data=json.dumps(my_data),
                                   content_type='application/json')
    token =  response.data['access']
    return token

@pytest.fixture(scope='function')
def attendant1():
    attendant1 = Attendant.objects.create(
                email='attendant1@me.com',
                username='attendant1',
                password='1234',
                first_name='Attendant1',
                last_name='Attendant1')
    return attendant1

@pytest.fixture
def get_or_create_attendant_token(db, client, attendant1):
    attendant1.save()
    url = reverse('authentication:token_obtain_pair')
    my_data =  {
        "email": "attendant1@me.com",
        "password": "1234"
	}
    response = client.post(url,data=json.dumps(my_data),
                                   content_type='application/json')
    token =  response.data['access']
    return token

@pytest.fixture(scope='function')
def accountant1():
    accountant1 = Accountant.objects.create(
                email='accountant1@me.com',
                username='accountant1',
                password='1234',
                first_name='Accountant1',
                last_name='Accountant1')
    return accountant1

@pytest.fixture
def get_or_create_accountant_token(db, client, accountant1):
    accountant1.save()
    url = reverse('authentication:token_obtain_pair')
    my_data =  {
        "email": "accountant1@me.com",
        "password": "1234"
	}
    response = client.post(url,data=json.dumps(my_data),
                                   content_type='application/json')
    token =  response.data['access']
    return token

@pytest.fixture(scope='function')
def store_keeper1():
    store_keeper1 = StoreKeeper.objects.create(
                email='store_keeper1@me.com',
                username='store_keeper1',
                password='1234',
                first_name='Storekeeper1',
                last_name='Storekeeper1')
    return store_keeper1

@pytest.fixture
def get_or_create_stoore_keeper_token(db, client, store_keeper1):
    store_keeper1.save()
    url = reverse('authentication:token_obtain_pair')
    my_data =  {
        "email": "store_keeper1@me.com",
        "password": "1234"
	}
    response = client.post(url,data=json.dumps(my_data),
                                   content_type='application/json')
    token =  response.data['access']
    return token

@pytest.fixture(scope='function')
def supervisor1():
    supervisor1 = Supervisor.objects.create(
                email='supervisor1@me.com',
                username='supervisor1',
                password='1234',
                first_name='Supervisor1',
                last_name='Supervisor1')
    return supervisor1

@pytest.fixture
def get_or_create_supervisor_token(db, client, supervisor1):
    supervisor1.save()
    url = reverse('authentication:token_obtain_pair')
    my_data =  {
        "email": "supervisor1@me.com",
        "password": "1234"
	}
    response = client.post(url,data=json.dumps(my_data),
                                   content_type='application/json')
    token =  response.data['access']
    return token
