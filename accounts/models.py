from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    type_choices = (('SYS', 'SYSADMIN'),
                    ('MEM', 'MEMBER'),
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
    gender_choices = (('M', 'MALE'),
                      ('F', 'FEMALE'),)
    user = models.OneToOneField(CustomUser)
    academy = models.ForeignKey(Academy)
    nick_name = models.CharField(max_length = 30)
    passport = models.CharField(max_length = 50)
    birthday = models.DateField()
    gender = models.CharField(max_length = 1,
                              choices = gender_choices,
                              default = 'M')
