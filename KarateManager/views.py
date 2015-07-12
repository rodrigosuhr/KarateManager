from django.shortcuts import render, render_to_response
from django.template import RequestContext

import xml.etree.ElementTree as ET

def home(request):
    tree = ET.parse('Associacao.XML')
    root = tree.getroot()
    return render_to_response('home.html', {'message': 'Whats up motherfuckers?'}, context_instance=RequestContext(request))
