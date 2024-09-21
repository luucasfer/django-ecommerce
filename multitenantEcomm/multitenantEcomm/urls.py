from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')), #Associa todas urls ao caminho padrão
    path('user/', include('userauths.urls')),
]

if settings.DEBUG:
    #Indica que todos os documentos STATIC estão no caminho da STATIC_URL 
    urlpatterns += static(settings.STATIC_URL, documents_root = settings.STATIC_ROOT)
    #Indica que todos as medias STATIC estão no caminho da MEDIA_URL
    urlpatterns += static(settings.MEDIA_URL, documents_root = settings.MEDIA_ROOT)