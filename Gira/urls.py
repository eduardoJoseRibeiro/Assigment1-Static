from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
from home.views import home

urlpatterns = [
    url(r'^$', home),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
