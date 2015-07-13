# -*- coding: utf-8 -*-
from django.shortcuts import render, render_to_response
from django.template import RequestContext

from django.contrib.auth.models import AbstractUser
from accounts.models import CustomUser as User, Confederation, Federation, Academy

import xml.etree.ElementTree as ET

def home(request):
    newUser = User.objects.create_user("CBKT", "secretaria@cbkt.org", "SECRETARIA@CBKT-KARATE")
    newUser.first_name = "Confederação Brasileira de Karatê-Dô Tradicional"
    newUser.user_type = "CON"
    newUser.save()

    newConf = Confederation()
    newConf.user = newUser
    newConf.country = "Brazil"
    newConf.save()

    newFed = ""

    cadastro = ET.parse('/home/rodrigo/Develop/Associacao.XML').getroot()
    for associacao in cadastro:
        username = associacao.find('cod').text.encode('utf8')
        email = associacao.find('email').text
        passwd = associacao.find('psw').text
        first_name = associacao.find('desc').text.encode('utf8')
        individual_limit = associacao.find('LmInd').text
        team_limit = associacao.find('LmEqp').text

        username = username[:2] if len(username)<=3 else username
        email = "karatemanagerapp@gmail.com" if email == None else email
        passwd = "NONONO" if passwd == None else passwd

        newUser = User.objects.create_user(username, email, passwd)
        newUser.first_name = first_name
        newUser.user_type = "FED" if len(username) == 2 else "ACA"
        newUser.save()

        if newUser == "FED":
            newFed = Federation()
            newFed.user = newUser
            newFed.confederation = newConf
            newFed.state = username[:2]
            newFed.individual_limit = individual_limit
            newFed.team_limit = team_limit
            newFed.save()
        else:
            newAca = Academy()
            newAca.user = newUser
            newAca.federation = newFed
            newAca.individual_limit = individual_limit
            newAca.team_limit = team_limit
            newAca.save()

    return render_to_response('home.html', {'message': 'Whats up motherfuckers?'}, context_instance=RequestContext(request))
