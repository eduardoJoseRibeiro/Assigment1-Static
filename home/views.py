# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from datetime import date

dt = date.today()

def home(request):
    context = {
        'page_name' : 'Home -',
        'year' : dt.year 
    }
    return render(request, 'index.html', context)

def contato(request):
    context = {
        'page_name' : 'Contato -',
        'year' : dt.year 
    }
    return render(request, 'contato.html', context)

def servicos(request):
    context = {
        'page_name' : 'Serviços -',
        'year' : dt.year
    }
    return render(request, 'servicos.html', context)