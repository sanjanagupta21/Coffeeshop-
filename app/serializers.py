from rest_framework import serializers
from .models import Reservation

class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        # fields = '__all__'  # Include all fields of the Reservation model
        fields = ['name', 'email', 'phone', 'date', 'time', 'guests']
