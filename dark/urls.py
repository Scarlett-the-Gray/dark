

from django.contrib import admin
from django.urls import include, path
from django.urls import re_path

urlpatterns = [
    path('darkhome/', include('darkhome.urls')),
    path('login/', include('login.urls')),
    path('admin/', admin.site.urls),
 
]


