from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    type_choices = (('MEM', 'MEMBER'),
                    ('ACA', 'ACADEMY'),
                    ('FED', 'FEDERATION'),
                    ('CON', 'CONFEDERATION'),)
    user_type = models.CharField(max_length = 3,
                                 choices = type_choices,
                                 default = 'MEM')

class Confederation(models.Model):
    user = models.OneToOneField(CustomUser)

class Federation(models.Model):
    user = models.OneToOneField(CustomUser)
    confederation = models.ForeignKey(Confederation)

class Academy(models.Model):
    user = models.OneToOneField(CustomUser)
    federation = models.ForeignKey(Federation)

class Member(models.Model):
    user = models.OneToOneField(CustomUser)
    academy = models.ForeignKey(Academy)
