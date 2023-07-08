from django.urls import path
from matriz import views

urlpatterns = [
    path('', views.home, name="home"),
    path('matriz/', views.matriz, name="matriz"),
    path('historico/', views.historico, name="historico"),
]