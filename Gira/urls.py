from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
from home.views import *

urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^contato$', contato, name='contato'),
    url(r'^planos$', planos, name='planos'),
    url(r'^sobre$', sobre, name='sobre'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
