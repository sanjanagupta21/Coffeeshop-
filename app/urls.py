from django.urls import path
from . import views
from .views import home, success, book_table,ReservationListCreate

urlpatterns = [
    path('', home, name='home'),
    
    # path('reservation/', views.reservation_view, name='reservation'),
    # path('reservation/', reservation_view, name='reservation'),
    path('reservation/', views.book_table, name='book_table'),
    path('success/', views.success, name='success'),
    path('api/reservations/', ReservationListCreate.as_view(), name='reservation-list-create'),
]
