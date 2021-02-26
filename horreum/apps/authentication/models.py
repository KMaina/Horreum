import uuid

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

# from horreum.utilities.base import CommonFieldsMixin


class User(AbstractUser):
    """Base class for all User types"""

    class Roles(models.TextChoices):
        """Different roles for the user types"""
        ATTENDANT = "ATTENDANT", "Attendant"
        CASHIER = "CASHIER", "Cashier"
        STORE_KEEPER = "STORE_KEEPER", "Store_keeper"
        ACCOUNTANT = "ACCOUNTANT", "Accountant"
        SUPERVISOR = "SUPERVISOR", "Supervisor"

    role = models.CharField(_("Role"), max_length=100, choices=Roles.choices, default=Roles.SUPERVISOR)
    email = models.EmailField(_("Email"), unique=True)
    is_deleted = models.BooleanField(default=False,
                                  help_text="This is to make sure deletes are not actual deletes")
    is_active = models.BooleanField(default=True)
    name = models.CharField(max_length=50, blank=False)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'password', 'first_name', 'last_name']


class AttendantManager(models.Manager):
    """Class to create attendant object & associated attributes"""
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(role=User.Roles.ATTENDANT)

class AccountantManager(models.Manager):
    """Class to create accountant object & associated attributes"""
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(role=User.Roles.ACCOUNTANT)

class CashierManager(models.Manager):
    """Class to create cashier object & associated attributes"""
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(role=User.Roles.CASHIER)

class StoreKeeperManager(models.Manager):
    """Class to create store keeper object & associated attributes"""
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(role=User.Roles.STORE_KEEPER)

class SupervisorManager(models.Manager):
    """Class to create manager object & associated attributes"""
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(role=User.Roles.SUPERVISOR)


class Attendant(User):
    """Class to create attendant object & associated attributes"""
    objects = AttendantManager()

    class Meta:
        proxy = True

    def save(self, *args, **kwargs):
        if not self.id:
            self.role = User.Roles.ATTENDANT
            self.set_password(self.password)
        return super().save(*args, **kwargs)

class Accountant(User):
    """Class to create attendant object & associated attributes"""
    objects = AccountantManager()

    class Meta:
        proxy = True

    def save(self, *args, **kwargs):
        if not self.id:
            self.role = User.Roles.ACCOUNTANT
            self.set_password(self.password)
        return super().save(*args, **kwargs)
    

class Cashier(User):
    """Class to create attendant object & associated attributes"""
    objects = CashierManager()

    class Meta:
        proxy = True

    def save(self, *args, **kwargs):
        if not self.pk:
            self.role = User.Roles.CASHIER
            self.set_password(self.password)
        return super().save(*args, **kwargs)
    
class StoreKeeper(User):
    """Class to create attendant object & associated attributes"""
    objects = StoreKeeperManager()

    def save(self, *args, **kwargs):
        if not self.pk:
            self.role = User.Roles.STORE_KEEPER
            self.set_password(self.password)
        return super().save(*args, **kwargs)
    
    class Meta:
        proxy = True

class Supervisor(User):
    objects = SupervisorManager()

    def save(self, *args, **kwargs):
        if not self.pk:
            self.role = User.Roles.SUPERVISOR
            self.set_password(self.password)
        return super().save(*args, **kwargs)
    
    class Meta:
        proxy = True

