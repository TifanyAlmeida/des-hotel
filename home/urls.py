from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.mostrar_home, name='home'),
    path('detalhes_hotel/<int:pk>', views.detalhes, name='detalhes')

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)