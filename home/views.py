# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render

def home(request):

    context = {
        'page_name' : 'Nome da Página'
    }

    return render(request, 'index.html', context)
