from django.conf.urls import url
from home import views

app_name = 'home'

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^contato$', views.contato, name='contato'),
    url(r'^planos$', views.planos, name='planos'),
    url(r'^sobre$', views.sobre, name='sobre'),
]