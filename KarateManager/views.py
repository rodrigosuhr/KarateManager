from django.shortcuts import render, render_to_response
from django.template import RequestContext

def home(request):
    return render_to_response('home.html', {'message': 'Whats up motherfuckers?'}, context_instance=RequestContext(request))
