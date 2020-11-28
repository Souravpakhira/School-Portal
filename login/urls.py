
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('register', views.register, name='register'),
    path('loginp', views.loginp, name='login'),
    path('logout', views.handleLogout, name='logout')
]
