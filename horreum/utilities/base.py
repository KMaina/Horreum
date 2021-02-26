from django.db import models

from django.contrib.auth.base_user import BaseUserManager


class CustomManager(models.Manager):
    """
    Filter in Custom manager so as not to return deleted objects
    """

    def get_queryset(self, *args, **kwargs):
        return super(CustomManager, self).get_queryset(*args, **kwargs).filter(deleted=False, is_active=True)

class CommonFieldsMixin(models.Model):
    """
    This contains all common fields
    Every model will inherit this to ensure DRY code
    Its abstract hence can't be instatiated
    """
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False,
                                  help_text="This is to make sure deletes are not actual deletes")
    is_active = models.BooleanField(default=True)
    everything = models.Manager()
    objects = CustomManager()

    def delete(self, *args, **kwargs):
        self.is_deleted = True
        self.is_active = False
        self.save()

    class Meta:
        ordering = ['-updated_at', '-created_at']
        abstract = True
