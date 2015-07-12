# -*- coding: utf-8 -*-
import pyboleto
import datetime
from pyboleto.bank.bancodobrasil import BoletoBB
from pyboleto.html import BoletoHTML

def get_invoice(bill_to, amount, due_date):
    d = BoletoBB(7, 2)
    d.nosso_numero = '0000000127'
    d.numero_documento = ''
    d.convenio = '2301731'
    d.especie_documento = 'DM'

    d.carteira = '18'
    d.cedente = 'Confederação Brasileira de Karatê-Dô Tradicional'
    d.cedente_documento = "35.795.707/0001-16"
    d.cedente_endereco = "Rua Acme, 123 - Centro - Sao Paulo/SP - CEP: 12345-678"
    d.agencia_cedente = '1458'
    d.conta_cedente = '189448'

    d.data_vencimento = datetime.date(2011, 10, 25)
    d.data_documento = datetime.date(2010, 2, 12)
    d.data_processamento = datetime.date(2010, 2, 12)

    d.instrucoes = [
        "- NÃO RECEBER APÓS 5 DIAS DE VENCIDO",
        "- APÓS O VENCIMENTO COBRAR 0,03% POR DIA DE ATRASO",
        "- APÓS O VENCIMENTO COBRAR MULTA DE 2%",
        ]
    d.demonstrativo = [
        "- Anuidades",
        ]
    d.valor_documento = 120.00

    d.sacado = [
        "Cliente Teste",
        ""
        ]
    return d
