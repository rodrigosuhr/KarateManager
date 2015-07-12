from django.shortcuts import render, render_to_response
from django.template import RequestContext
from payments.invoices import get_invoice
from pyboleto.html import BoletoHTML

def home(request):
    invoice = get_invoice('', 255.00, '')
    invoice_HTML = BoletoHTML('boleto-bb-normal-teste.html')
    invoice_HTML.drawBoleto(invoice)
    invoice_HTML.save()
    return render_to_response('home.html', context_instance=RequestContext(request))
