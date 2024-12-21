from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('vulnerable-sql/', views.vulnerable_sql, name='vulnerable_sql'),
    path('hardcoded-secret/', views.hardcoded_secret, name='hardcoded_secret'),
]

