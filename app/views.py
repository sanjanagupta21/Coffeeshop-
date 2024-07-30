from django.shortcuts import render
def home(request):
    return render(request, 'home.html')

def reservation(request):
    return render(request,'reservation.html')

# Create your views here.
