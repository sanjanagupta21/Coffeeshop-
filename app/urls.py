from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_view, name='home'),  # Directs to home page
    path('menu/', views.menu_view, name='menu'),  # Directs to menu page
]

urlpatterns = [
    path('menu/', views.menu_view, name='menu'),
    path('add-to-cart/', views.add_to_cart, name='add_to_cart'),
    path('', views.home_view, name='home'),
    path('add-to-cart/', views.add_to_cart, name='add_to_cart'),
]
