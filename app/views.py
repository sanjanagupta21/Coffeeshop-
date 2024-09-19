from django.shortcuts import render, redirect
def home(request):
    return render(request, 'home.html')


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
    
