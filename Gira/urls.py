from django.conf.urls import url, include
from django.conf.urls.static import static
from django.conf import settings
from home import urls 

urlpatterns = [
    url(r'^', include('home.urls', namespace="home"))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
