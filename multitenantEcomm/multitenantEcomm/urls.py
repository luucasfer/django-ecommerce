"""
URL configuration for multitenantEcomm project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')), #Associa todas urls ao caminho padrão
]

if settings.DEBUG:
    #Indica que todos os documentos STATIC estão no caminho da STATIC_URL 
    urlpatterns += static(settings.STATIC_URL, documents_root = settings.STATIC_ROOT)
    #Indica que todos as medias STATIC estão no caminho da MEDIA_URL
    urlpatterns += static(settings.MEDIA_URL, documents_root = settings.MEDIA_ROOT)