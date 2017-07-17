from django.db import models
from django.contrib import auth
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser)
from django.contrib.auth.models import Group
from django.contrib.auth.models import PermissionsMixin
from django.contrib.contenttypes.models import ContentType
from django.core.exceptions import PermissionDenied
from django.contrib.auth.models import User
from api import actions
import requests
import json

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
import oeplatform.securitysettings as sec
import dataedit.models as datamodels

NO_PERM = 0
WRITE_PERM = 4
DELETE_PERM = 8
ADMIN_PERM = 12


class UserManager(BaseUserManager):
    def create_user(self, name, mail_address, affiliation=None):
        if not mail_address:
            raise ValueError('An email address must be entered')
        if not name:
            raise ValueError('A name must be entered')

        user = self.model(name=name, mail_address=self.normalize_email(mail_address),
                          affiliation=affiliation, )

        user.save(using=self._db)
        return user

    def create_superuser(self, name, mail_address, affiliation):

        user = self.create_user(name, mail_address,
                                affiliation=affiliation)
        user.is_admin = True
        user.save(using=self._db)
        return user


class PermissionHolder():


    def has_write_permissions(self, schema, table):
        """
        This function returns the authorization given the schema and table.
        """
        return self.__get_perm(schema, table) >= WRITE_PERM

    def has_delete_permissions(self, schema, table):
        """
        This function returns the authorization given the schema and table.
        """
        return self.__get_perm(schema, table) >= DELETE_PERM

    def has_admin_permissions(self, schema, table):
        """
        This function returns the authorization given the schema and table.
        """
        return self.__get_perm(schema, table) >= ADMIN_PERM

    def __get_perm(self, schema, table):
        perm = self.table_permissions.filter(table__name=table,
                                   table__schema__name=schema).first()
        if perm:
            return perm.permission
        else:
            return NO_PERM


class UserGroup(Group, PermissionHolder):
    description = models.TextField(null=False, default='')


class TablePermission(models.Model):
    choices = ((NO_PERM, 'None'),
               (WRITE_PERM, 'Write'),
               (DELETE_PERM, 'Delete'),
               (ADMIN_PERM, 'Admin'))
    table = models.ForeignKey(datamodels.Table)

    level = models.IntegerField(choices=choices,
                                     default=NO_PERM)


    class Meta:
        unique_together = (('table', 'holder'),)
        abstract = True


class myuser(AbstractBaseUser, PermissionHolder):
    name = models.CharField(max_length=50, unique=True)
    affiliation = models.CharField(max_length=50, null=True)
    mail_address = models.EmailField(verbose_name='email address',
                                     max_length=255, unique=True, )

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'name'

    REQUIRED_FIELDS = [name]

    if sec.DEBUG:
        objects = UserManager()

    def get_full_name(self):
        return self.name

    def get_short_name(self):
        return self.name

    def __str__(self):  # __unicode__ on Python 2
        return self.name

    @property
    def is_staff(self):
        return self.is_admin


class UserPermission(TablePermission):
    holder = models.ForeignKey(myuser,
                               related_name='table_permissions')


class GroupPermission(TablePermission):
    holder = models.ForeignKey(UserGroup,
                               related_name='table_permissions')

class GroupMembership(models.Model):
    choices = ((NO_PERM, 'None'),
               (WRITE_PERM, 'Invite'),
               (DELETE_PERM, 'Remove'),
               (ADMIN_PERM, 'Admin'))
    user = models.ForeignKey(myuser, related_name='memberships')
    group = models.ForeignKey(UserGroup, related_name='memberships')
    level = models.IntegerField(choices=choices,
                                default=WRITE_PERM)

class UserBackend(object):
    def authenticate(self, username=None, password=None):
        url = 'https://wiki.openmod-initiative.org/api.php?action=login'
        data = {'format':'json', 'lgname':username}

        #A first request to receive the required token
        token_req = requests.post(url, data)
        data['lgpassword'] = password
        data['lgtoken'] = token_req.json()['login']['token']

        # A second request for the actual authentication
        login_req = requests.post(url, data, cookies=token_req.cookies)

        if login_req.json()['login']['result'] == 'Success':
            return myuser.objects.get_or_create(name=username)[0]
        else:
            return None


    def get_user(self, user_id):
        try:
            return myuser.objects.get(pk=user_id)
        except myuser.DoesNotExist:
            return None

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

