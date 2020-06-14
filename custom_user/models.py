from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from django.db.models import CharField,  ForeignKey
from django.db.models.signals import post_save
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
from django.dispatch import receiver
from django.core.exceptions import ValidationError

from wagtail.core.models import Page, GroupPagePermission, GroupCollectionPermission, Collection

class User(AbstractUser):
    name = CharField(_("Name of User"), blank=True, max_length=255)
    
    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"username": self.username})