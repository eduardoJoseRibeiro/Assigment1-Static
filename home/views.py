# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from datetime import date

dt = date.today()

def home(request):
    context = {
        'page_name' : 'Home -',
        'year' : dt.year,
        'link_ativo' : 'home'
    }
    return render(request, 'index.html', context)

def contato(request):
    context = {
        'page_name' : 'Contato -',
        'year' : dt.year,
        'link_ativo' : 'contato'
    }
    return render(request, 'contato.html', context)

def planos(request):
    context = {
        'page_name' : 'Conheça nossos Planos -',
        'year' : dt.year,
        'link_ativo' : 'planos'
    }
    return render(request, 'planos.html', context)

def sobre(request):
    context = {
        'page_name' : 'Saiba mais sobre nós -',
        'year' : dt.year,
        'link_ativo' : 'sobre'
    }
    return render(request, 'sobre.html', context)