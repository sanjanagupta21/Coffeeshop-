from django.shortcuts import render, redirect
def home(request):
    return render(request, 'home.html')

def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')




# def reservation(request):
#     return render(request,'reservation.html')

# def reservation_view(request):
#     if request.method == 'POST':
#         # Handle form submission here
#         name = request.POST.get('name')
#         email = request.POST.get('email')
#         date = request.POST.get('date')
#         time = request.POST.get('time')
#         persons = request.POST.get('persons')
        # Process the form data (e.g., save to the database)
        

# from .forms import BookingForm

# def reservation(request):
#     if request.method == 'POST':
#         form = BookingForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('success')
#     else:
#         form = BookingForm()
#     return render(request, 'reservation.html', {'form': form})


    
    # return render(request, 'reservation.html')
# from django.shortcuts import render, redirect
# from django.contrib import messages
# from .forms import ReservationForm
# from .models import Reservation

# def book_table(request):
#     if request.method == 'POST':
#         print("POST data:", request.POST)
#         form = ReservationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             # messages.success(request, 'Your table has been booked successfully!')
#             return redirect('success')
#         else:
#             print(form.errors)
#     else:
#         form = ReservationForm()

#     return render(request, 'reservation.html', {'form': form})

from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Reservation  
# def book_table(request):
#     if request.method=='POST':
#         name=request.POST.get('name')
#         email=request.POST.get('email')
#         phone=request.POST.get('phone')
#         date=request.POST.get('date')
#         time=request.POST.get('time')
#         guests=request.POST.get('guests')
        
#         Reservation.objects.create(
#             name=name,
#             email=email,
#             phone=phone,
#             date=date,
#             time=time,
#             guests=guests
#         )
#         return redirect('success')
#         print("+++++++++++++++++====================++++++++++++++")
#         print("name: ",name)
#         print("email: ",email)
#     return render(request, 'reservation.html')
    
# def book_table(request):
#     if request.method == 'POST':
#         form = ReservationForm(request.POST)
#         if form.is_valid():
#             # Save the form data to the database
#             Reservation.objects.create(
#                 name=form.cleaned_data['name'],
#                 email=form.cleaned_data['email'],
#                 phone=form.cleaned_data['phone'],
#                 date=form.cleaned_data['date'],
#                 time=form.cleaned_data['time'],
#                 guests=form.cleaned_data['guests']
#             )
#             return redirect('success')
#     else:
#         form = ReservationForm()

#     return render(request, 'reservation.html', {'form': form})

from .serializers import ReservationSerializer
def success(request):
    return render(request, 'success.html')

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Reservation
from .serializers import ReservationSerializer

class ReservationListCreate(APIView):
    def get(self, request):
        reservations = Reservation.objects.all()
        serializer = ReservationSerializer(reservations, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = ReservationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# def book_table(request):
    # if request.method == 'POST':
    #     form = Reservation(request.POST)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return JsonResponse({'success': True})
    #     else:
    #         return JsonResponse({'success': False, 'errors': form.errors})
    # return render(request, 'reservation.html', {'form': Reservation()})

# Create your views here.

def book_table(request):
    # if request.method == 'POST':
    #     serializer = ReservationSerializer(data=request.POST)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return JsonResponse({'success': True})
    #     else:
    #         return JsonResponse({'success': False, 'errors': serializer.errors})
    
    # return render(request, 'reservation.html', {'form': ReservationSerializer()})
    if request.method == 'POST':
        serializer = ReservationSerializer(data=request.POST)
        if serializer.is_valid():
            print("Data is valid. Attempting to save...")
            serializer.save()
            print("Data saved successfully.")
            return JsonResponse({'success': True, 'message': 'Table booked successfully!'})
        else:
            print("Validation errors:", serializer.errors)
            return JsonResponse({'success': False, 'message': 'There was an error booking your table. Please try again.', 'errors': serializer.errors})
    
    return render(request, 'reservation.html')


# import random
# from django.conf import settings
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from .serializers import *
# from .models import User
# from django.core.mail import send_mail

# class RegisterAPI(APIView):
#     def post(self, request):
#         try:
#             data = request.data
#             serializer = UserSerializer(data=data)

#             if serializer.is_valid():
#                 user = serializer.save()
#                 otp = random.randint(1000, 9999)
#                 user.otp = str(otp)
#                 user.save()

#                 subject = 'Your account verification email'
#                 message = f'Your OTP is {otp}'
#                 email_from = settings.EMAIL_HOST_USER
#                 send_mail(subject, message, email_from, [user.email], fail_silently=False)
#                 return Response({
#                     'status': status.HTTP_201_CREATED,
#                     'msg': 'Registration successful. Check your email for the OTP.',
#                     'data': serializer.data
#                 }, status=status.HTTP_201_CREATED)

#             return Response({
#                 'status': status.HTTP_400_BAD_REQUEST,
#                 'msg': 'Invalid data',
#                 'data': serializer.errors
#             }, status=status.HTTP_400_BAD_REQUEST)

#         except Exception as e:
#             return Response({
#                 'status': status.HTTP_500_INTERNAL_SERVER_ERROR,
#                 'msg': str(e),
#                 'data': None
#             }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            
# class VerifyOtp(APIView):
    
#     def post(self, request):
#         try:
#             data = request.data
#             serializer = VerifyOtpSerializer(data=data)
#             if serializer.is_valid():
#                 email = serializer.data['email']
#                 otp = serializer.data['otp']
#                 user = User.objects.filter(email=email).first()

#                 if not user:
#                     return Response({
#                         'status': status.HTTP_400_BAD_REQUEST,
#                         'msg': 'Invalid email',
#                         'data': 'The provided email does not exist in our records.'
#                     }, status=status.HTTP_400_BAD_REQUEST)

#                 if user.otp != otp:
#                     return Response({
#                         'status': status.HTTP_400_BAD_REQUEST,
#                         'msg': 'Wrong OTP',
#                         'data': 'The OTP you provided is incorrect.'
#                     }, status=status.HTTP_400_BAD_REQUEST)

#                 user.is_verified = True
#                 user.save()
#                 return Response({
#                     'status': status.HTTP_200_OK,
#                     'msg': 'Account verified successfully',
#                     'data': serializer.data
#                 }, status=status.HTTP_200_OK)
#             else:
#                 return Response({
#                     'status': status.HTTP_400_BAD_REQUEST,
#                     'msg': 'Invalid data',
#                     'data': serializer.errors
#                 }, status=status.HTTP_400_BAD_REQUEST)

#         except Exception as e:
#             return Response({
#                 'status': status.HTTP_500_INTERNAL_SERVER_ERROR,
#                 'msg': str(e),
#                 'data': None
#             }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
# from app.emails import send_otp_via_email
# class EmailTest(APIView):
#     def get(self, request):
#         print("hello world")
#         email = send_otp_via_email("sanjanagupta2003.4@gmail.com")
#         return Response("hello")

# import random
# from django.conf import settings
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from .serializers import UserSerializer, VerifyOtpSerializer
# from .models import User
# from django.core.mail import send_mail

# # Registration API
# class RegisterAPI(APIView):
#     def post(self, request):
#         try:
#             data = request.data
#             serializer = UserSerializer(data=data)
            
#             if serializer.is_valid():
#                 # Save the user but set verified to False
#                 user = serializer.save()
#                 user.is_verified = False
                
#                 # Generate OTP
#                 otp = random.randint(1000, 9999)
#                 user.otp = str(otp)
#                 user.save()

#                 # Send OTP via email
#                 subject = 'Your account verification OTP'
#                 message = f'Your OTP is {otp}'
#                 email_from = settings.EMAIL_HOST_USER
#                 send_mail(subject, message, email_from, [user.email], fail_silently=False)

#                 return Response({
#                     'status': status.HTTP_201_CREATED,
#                     'msg': 'Registration successful. Check your email for the OTP.',
#                     'data': serializer.data
#                 }, status=status.HTTP_201_CREATED)

#             return Response({
#                 'status': status.HTTP_400_BAD_REQUEST,
#                 'msg': 'Invalid data',
#                 'data': serializer.errors
#             }, status=status.HTTP_400_BAD_REQUEST)

#         except Exception as e:
#             return Response({
#                 'status': status.HTTP_500_INTERNAL_SERVER_ERROR,
#                 'msg': str(e),
#                 'data': None
#             }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# # OTP Verification API for Registration
# class VerifyOtpAPI(APIView):
#     def post(self, request):
#         try:
#             data = request.data
#             serializer = VerifyOtpSerializer(data=data)
#             if serializer.is_valid():
#                 email = serializer.data['email']
#                 otp = serializer.data['otp']
#                 user = User.objects.filter(email=email).first()

#                 if not user:
#                     return Response({
#                         'status': status.HTTP_400_BAD_REQUEST,
#                         'msg': 'Invalid email',
#                         'data': 'User does not exist.'
#                     }, status=status.HTTP_400_BAD_REQUEST)

#                 if user.otp != otp:
#                     return Response({
#                         'status': status.HTTP_400_BAD_REQUEST,
#                         'msg': 'Invalid OTP',
#                         'data': 'Incorrect OTP.'
#                     }, status=status.HTTP_400_BAD_REQUEST)

#                 # Mark user as verified
#                 user.is_verified = True
#                 user.save()
#                 return Response({
#                     'status': status.HTTP_200_OK,
#                     'msg': 'Account verified successfully',
#                     'data': {'email': email}
#                 }, status=status.HTTP_200_OK)
#             else:
#                 return Response({
#                     'status': status.HTTP_400_BAD_REQUEST,
#                     'msg': 'Invalid data',
#                     'data': serializer.errors
#                 }, status=status.HTTP_400_BAD_REQUEST)

#         except Exception as e:
#             return Response({
#                 'status': status.HTTP_500_INTERNAL_SERVER_ERROR,
#                 'msg': str(e),
#                 'data': None
#             }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# # Login API to Send OTP
# class LoginAPI(APIView):
#     def post(self, request):
#         try:
#             email = request.data.get('email')

#             user = User.objects.filter(email=email).first()
#             if not user:
#                 return Response({
#                     'status': status.HTTP_400_BAD_REQUEST,
#                     'msg': 'Invalid email',
#                     'data': 'User does not exist.'
#                 }, status=status.HTTP_400_BAD_REQUEST)

#             if not user.is_verified:
#                 return Response({
#                     'status': status.HTTP_400_BAD_REQUEST,
#                     'msg': 'Account not verified',
#                     'data': 'Please verify your account first.'
#                 }, status=status.HTTP_400_BAD_REQUEST)

#             # Generate OTP and send email
#             otp = random.randint(1000, 9999)
#             user.otp = str(otp)
#             user.save()

#             # Send OTP via email
#             subject = 'Your login OTP'
#             message = f'Your OTP is {otp}'
#             email_from = settings.EMAIL_HOST_USER
#             send_mail(subject, message, email_from, [user.email], fail_silently=False)

#             return Response({
#                 'status': status.HTTP_200_OK,
#                 'msg': 'OTP sent to your email.',
#             }, status=status.HTTP_200_OK)

#         except Exception as e:
#             return Response({
#                 'status': status.HTTP_500_INTERNAL_SERVER_ERROR,
#                 'msg': str(e),
#                 'data': None
#             }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# # OTP Verification API for Login
# class VerifyLoginOtpAPI(APIView):
#     def post(self, request):
#         try:
#             data = request.data
#             serializer = VerifyOtpSerializer(data=data)

#             if serializer.is_valid():
#                 email = serializer.data['email']
#                 otp = serializer.data['otp']
#                 user = User.objects.filter(email=email).first()

#                 if not user:
#                     return Response({
#                         'status': status.HTTP_400_BAD_REQUEST,
#                         'msg': 'Invalid email',
#                         'data': 'User does not exist.'
#                     }, status=status.HTTP_400_BAD_REQUEST)

#                 if user.otp != otp:
#                     return Response({
#                         'status': status.HTTP_400_BAD_REQUEST,
#                         'msg': 'Invalid OTP',
#                         'data': 'Incorrect OTP.'
#                     }, status=status.HTTP_400_BAD_REQUEST)

#                 return Response({
#                     'status': status.HTTP_200_OK,
#                     'msg': 'Login successful',
#                     'data': {'email': email}
#                 }, status=status.HTTP_200_OK)

#             return Response({
#                 'status': status.HTTP_400_BAD_REQUEST,
#                 'msg': 'Invalid data',
#                 'data': serializer.errors
#             }, status=status.HTTP_400_BAD_REQUEST)

#         except Exception as e:
#             return Response({
#                 'status': status.HTTP_500_INTERNAL_SERVER_ERROR,
#                 'msg': str(e),
#                 'data': None
#             }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            
            
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# import random
# from django.core.mail import send_mail
# from .models import User, UserOTP
# from django.utils import timezone

# # Register view to send OTP
# class RegisterView(APIView):
#     def post(self, request):
#         email = request.data.get('email')
#         if not email:
#             return Response({"error": "Email is required"}, status=status.HTTP_400_BAD_REQUEST)
        
#         otp = random.randint(100000, 999999)  # Generate a random 6-digit OTP
        
#         # Save OTP to the database with timestamp
#         UserOTP.objects.create(email=email, otp=otp, timestamp=timezone.now())
        
#         # Send OTP via email
#         send_mail(
#             'Your OTP Code',
#             f'Your OTP code is {otp}',
#             'your-email@example.com',  # Replace with your email
#             [email],
#             fail_silently=False,
#         )
        
#         return Response({"message": "OTP has been sent to your email"}, status=status.HTTP_200_OK)

# # OTP Verification View
# class VerifyOTPView(APIView):
#     def post(self, request):
#         email = request.data.get('email')
#         otp = request.data.get('otp')
        
#         if not email or not otp:
#             return Response({"error": "Email and OTP are required"}, status=status.HTTP_400_BAD_REQUEST)
        
#         # Check if OTP exists and is valid
#         try:
#             user_otp = UserOTP.objects.get(email=email, otp=otp)
#             # Add logic for checking if OTP has expired (optional)
#             user_otp.delete()  # OTP is single-use, so delete it after verification
            
#             # Register the user or save their email to the database
#             # Assuming you have a User model
#             user, created = User.objects.get_or_create(email=email)
            
#             return Response({"message": "OTP verified successfully!"}, status=status.HTTP_200_OK)
#         except UserOTP.DoesNotExist:
#             return Response({"error": "Invalid OTP"}, status=status.HTTP_400_BAD_REQUEST)

from django.shortcuts import render, redirect
from .models import User  # Import your User model
from django.contrib import messages  # Optional for feedback

from django.shortcuts import render, redirect
from .models import User  # Adjust the import according to your User model's location
from django.contrib import messages  # Optional for feedback
from django.contrib.auth.hashers import make_password  # For password hashing
from django.shortcuts import render, redirect
from .models import User  # Adjust the import according to your User model's location
from django.contrib import messages  # Optional for feedback
from django.contrib.auth.hashers import make_password  # For password hashing

# def register(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         email = request.POST.get('email')
#         password = request.POST.get('password')
        
#         if User.objects.filter(username=username).exists():
#             messages.error(request, "Username already exists.")
#         elif User.objects.filter(email=email).exists():
#             messages.error(request, "Email already registered.")
#         else:
#             user = User(username=username, email=email)  # Create the user object without password
#             user.password = make_password(password)  # Manually hash the password and assign it
#             user.save()  # Save the user to the database
#             messages.success(request, "Registration successful!")
#             return redirect('login')  # Redirect to the login page
        
#     return render(request, 'register.html')

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
        elif User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered.")
        else:
            # Use the UserManager to create a new user
            user = User.objects.create_user(email=email, username=username, password=password)
            messages.success(request, "Registration successful!")
            return redirect('login')
        
    return render(request, 'register.html')

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

# def login_view(request):
#     if request.method == 'POST':
#         email = request.POST.get('email')
#         password = request.POST.get('password')

#         # Authenticate user using email and password
#         user = authenticate(request, username=email, password=password)

#         if user is not None:
#             login(request, user)  # Log the user in using the authenticated user object
#             messages.success(request, "Login successful!")
#             return redirect('home')  # Redirect to a home page after login (adjust as needed)
#         else:
#             messages.error(request, "Invalid email or password.")
    
#     return render(request, 'login.html')

from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Authenticate user using email and password
        user = authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "Login successful!")
            return redirect('home')  # Redirect to home page after login
        else:
            messages.error(request, "Invalid email or password.")
    
    return render(request, 'login.html')

from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def profile(request):
    return render(request, 'profile.html')



