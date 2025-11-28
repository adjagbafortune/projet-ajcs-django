from django.contrib import admin
from django.urls import path
from app_auth import views
from django.urls import path


urlpatterns = [
    path('admin/', admin.site.urls),
    path('inscription/', views.inscription, name='inscription'),
    path('', views.connexion, name='connexion'),
    path('acceuil/', views.acceuil, name='acceuil'),
    path('deconnexion/', views.deconnexion, name='deconnexion'),
]