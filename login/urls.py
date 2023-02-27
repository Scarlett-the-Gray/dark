from django.urls import path, include
from django.contrib.auth import views as auth_views
from login import views

app_name = 'django.contrib.auth'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('register/', views.register_user, name='register_user'),
    path('authenticate_user/', views.authenticate_user,name='authenticate_user'),
    path('login/', include("django.contrib.auth.urls")),
    path('logout/', views.user_logout, name='logout'),
]