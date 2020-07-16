import random
import string

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.core import validators
from django.db import models
from django.core.validators import RegexValidator
from django.utils.translation import ugettext_lazy as _

from safedelete.config import HARD_DELETE
from .managers import UserManager
from lib.models import BaseSafeDeleteModel


def user_directory_path(instance, filename): 
    return 'user_{0}/{1}'.format(instance.id, filename)


def user_file_directory_path(instance, filename): 
    return 'user_{0}/{1}'.format(instance.user.id, filename) 


class User(AbstractBaseUser, PermissionsMixin, BaseSafeDeleteModel):

    GENDER_CHOICES = (
        ('M', 'Mulher'),
        ('H', 'Homem'),
        ('MT', 'Mulher Trans'),
        ('HT', 'Homem Trans')
    )


    name = models.CharField(_('nome'), max_length=100, null=True, blank=True)
    email = models.EmailField(_('e-mail'), unique=True)
    username = models.CharField(_('username'), max_length=30, unique=True,
        help_text=_('Required. 30 characters or fewer. Letters, digits and '
                    '@/./+/-/_ only.'),
        validators=[
            validators.RegexValidator(r'^[\w.@+-]+$',
                                      _('Enter a valid username. '
                                        'This value may contain only letters, numbers '
                                        'and @/./+/-/_ characters.'), 'invalid'),
        ],
        error_messages={
            'unique': _("A user with that username already exists."),
        })
    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_('Designates whether the user can log into '
                    'this admin site.'))
    cpf = models.CharField(_('CPF'), max_length=14)
    telephone = models.CharField(_('Telefone'), max_length=12, blank=True)
    birth_date = models.DateField()
    gender = models.CharField(max_length=2, choices=GENDER_CHOICES, blank=True, null=True)
    is_first_login = models.BooleanField(default=True)

    objects =  UserManager()


    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        if self.name == None:
            return str(self.username)
        return str(self.name)

