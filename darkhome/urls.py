from django.urls import path
from . import views

urlpatterns = [
    path('homepage/', views.homepage, name='homepage'),
    path('album/', views.album, name='album'),
    path('contact/', views.contact, name='contact'),
]