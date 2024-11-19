from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from apps.inbox import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'), 
    path('cotizador/', include('apps.cotizador.urls')),
    path('payments/', include('apps.payments.urls')),   
    path('weather/', include('apps.weather.urls')),   
]


# Agrega este bloque para servir archivos estáticos durante el desarrollo
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)