from rest_framework import serializers
from .models import Reservation, User

class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        # fields = '__all__'  # Include all fields of the Reservation model
        fields = ['name', 'email', 'phone', 'date', 'time', 'guests']
        
        
# from rest_framework import serializers
# from django.contrib.auth.hashers import make_password
# from .models import User

# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['email', 'password']

#     def create(self, validated_data):
#         validated_data['password'] = make_password(validated_data['password'])
#         return super(UserSerializer, self).create(validated_data)

# class VerifyOtpSerializer(serializers.Serializer):
#     email = serializers.EmailField()
#     otp = serializers.CharField(max_length=6)
    
    
# from rest_framework import serializers
# from .models import User

# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['email', 'password']

#     def create(self, validated_data):
#         user = User(**validated_data)
#         user.set_password(validated_data['password'])  # Hash the password
#         user.save()
#         return user

# class VerifyOtpSerializer(serializers.Serializer):
#     email = serializers.EmailField()
#     otp = serializers.CharField(max_length=4)


    



# class UserSerializer(serializers.ModelSerializer):

#     class Meta:
#         model=User
#         fields=['email','is_verified']
#     def create(self, validated_data):
#         user = User.objects.create_user(**validated_data)
#         return user

# class VerifyOtpSerializer(serializers.Serializer):
#     email=serializers.EmailField()
#     otp=serializers.CharField(max_length=6)