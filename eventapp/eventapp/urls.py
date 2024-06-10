"""
URL configuration for eventapp project.

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
from app.views import index, add_event, edit_event, delete_event
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', index, name='index'),
    path('add_event/', add_event, name='add_event'),
    path('edit_event/<event_id>', edit_event, name='edit_event'),
    path('delete_event/<event_id>', delete_event, name='delete_event')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
