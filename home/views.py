# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from datetime import date

dt = date.today()

def home(request):

    context = {
        'page_name' : 'Nome da Página',
        'year' : dt.year 
    }

    return render(request, 'index.html', context)
