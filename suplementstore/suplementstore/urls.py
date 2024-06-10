"""
URL configuration for suplementstore project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from store_app.views import index, supplements, supplement_details, edit_supplement, add_supplement, delete_supplement
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', index, name='index'),
    path('supplements/', supplements, name='supplements'),
    path('add_supplement/', add_supplement, name='add_supplement'),
    path('edit_supplement/<supplement_id>', edit_supplement, name='edit_supplement'),
    path('delete_supplement/<supplement_id>', delete_supplement, name='delete_supplement'),
    path('supplement_details/<supplement_id>', supplement_details, name='supplement_details'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
