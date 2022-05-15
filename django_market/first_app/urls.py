from django.urls import path
from . import views

urlpatterns = [
    path('', views.shop, name='shop'),
    path('support/', views.support, name='sup'),
    path('logout/', views.logout, name='logout'),
    path('developers/', views.developers, name='dev'),
]