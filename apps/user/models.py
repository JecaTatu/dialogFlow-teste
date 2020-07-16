import random
import string

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.core import validators
from django.db import models
from django.core.validators import RegexValidator
from django.utils.translation import ugettext_lazy as _

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
    cpf = models.CharField(_('CPF'), max_length=14, blank=True, null=True)
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


class Complaint(BaseSafeDeleteModel):
    user = models.ForeignKey(to="User", on_delete=models.DO_NOTHING, blank=True, null=True)
    description = models.CharField(_('Descrição'), max_length=300, blank=True, null=True)
    # geo_location = models.PointField(_('Endereço onde está ocorrendo'),blank=True, null=True)
    address = models.CharField(_('Endereço do ocorrido'), max_length=30, blank=True, null=True)
    when_happen = models.DateField(_("Dia do ocorrido"), blank=True, null=True)
    time_when_happen = models.TimeField(_("Horário do ocorrido"), blank=True, null=True)
    bus_number = models.CharField(_("Número do ônibus"), max_length=30, blank=True, null=True)
    bus_license_plate = models.CharField(_("Placa do ônibus"), max_length=30, blank=True, null=True)
    video_or_image = models.FileField(_("Vídeo ou imagem do ocorrido"), 
        upload_to=user_file_directory_path, blank=True, null=True
    )