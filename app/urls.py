from django.urls import path
from . import views
from .views import home, success,register, book_table,ReservationListCreate,login_view
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', home, name='home'),
    
    # path('reservation/', views.reservation_view, name='reservation'),
    # path('reservation/', reservation_view, name='reservation'),
    path('reservation/', views.book_table, name='book_table'),
    path('login/', views.login_view, name='login'),
    path('success/', views.success, name='success'),
    path('api/reservations/', ReservationListCreate.as_view(), name='reservation-list-create'),
    # path('register/', RegisterAPI.as_view(), name='register'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    
    # path('api/register/', RegisterView.as_view(), name='register'),
    # path('verify-otp/', VerifyOtpAPI.as_view(), name='verify_otp'),
    # path('login/', LoginAPI.as_view(), name='login'),
    # path('verify-login-otp/', VerifyLoginOtpAPI.as_view(), name='verify_login_otp'),
    # path('api/verify-otp/', VerifyOTPView.as_view(), name='verify_otp'),
#     path('email_test/',EmailTest.as_view(), name='email_test')


# ]

]
