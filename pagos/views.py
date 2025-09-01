from django.shortcuts import render
from .models import Pago, Webhook

def lista_pagos(request):
    pagos = Pago.objects.all()
    return render(request, 'pagos/pagos.html', {'pagos': pagos})

def lista_webhooks(request):
    webhooks = Webhook.objects.all()
    return render(request, 'pagos/webhooks.html', {'webhooks': webhooks})
