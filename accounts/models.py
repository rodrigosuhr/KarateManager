from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    type_choices = (('SYS', 'SYSADMIN'),
                    ('MEM', 'MEMBER'),
                    ('ACA', 'ACADEMY'),
                    ('FED', 'FEDERATION'),
                    ('CON', 'CONFEDERATION'),)
    user_type = models.CharField(max_length=3,
                                 choices=type_choices,
                                 default='MEM')

class Confederation(models.Model):
    user = models.OneToOneField(CustomUser)
    country = models.CharField(max_length=30)

class Federation(models.Model):
    user = models.OneToOneField(CustomUser)
    confederation = models.ForeignKey(Confederation)
    state = models.CharField(max_length=3)
    individual_limit = models.IntegerField()
    team_limit = models.IntegerField()

class Academy(models.Model):
    user = models.OneToOneField(CustomUser)
    federation = models.ForeignKey(Federation)
    individual_limit = models.IntegerField()
    team_limit = models.IntegerField()

class Member(models.Model):
    gender_choices = (('M', 'MALE'),
                      ('F', 'FEMALE'),)
    role_choices = (('ATL', 'ATHLETE'),
                    ('INS', 'INSTRUCTOR'),
                    ('REF', 'REFEREE'),
                    ('COA', 'COACH'),
                    ('BOA', 'BOARD MEMBER'),
                    ('DEL', 'DELEGATE'),
                    ('JUD', 'JUDGE'),
                    ('DIR', 'DIRECTOR'),)
    status_choices = (('COM', 'COMPLIANT'),
                      ('DEF', 'DEFAULTER'),)
    user = models.OneToOneField(CustomUser)
    academy = models.ForeignKey(Academy)
    nick_name = models.CharField(max_length=30)
    passport = models.CharField(max_length=50)
    birthday = models.DateField()
    gender = models.CharField(max_length=1,
                              choices=gender_choices,
                              default='M')
    registration = models.CharField(max_length=30)
    created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    role = models.CharField(max_length=3, choices=role_choices)
