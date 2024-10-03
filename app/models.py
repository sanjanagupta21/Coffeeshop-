

from django.db import models

class Reservation(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    date = models.DateField()
    time = models.TimeField()
    guests = models.IntegerField()
    test = models.CharField(null=True,blank=True,max_length=250)

    def __str__(self):
        return f"Reservation for {self.name} on {self.date} at {self.time}"
    
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models

# class UserManager(BaseUserManager):
#     def create_user(self, email, **extra_fields):
#         """
#         Create and return a regular user with the given email.
#         """
#         if not email:
#             raise ValueError('The Email field must be set')
#         email = self.normalize_email(email)
#         user = self.model(email=email, **extra_fields)
#         # user.set_password(password)  # Remove or comment this line
#         user.save(using=self._db)
#         return user

#     def create_superuser(self, email, password=None, **extra_fields):
#         """
#         Create and return a superuser with the given email and password.
#         """
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_superuser', True)

#         if extra_fields.get('is_staff') is not True:
#             raise ValueError('Superuser must have is_staff=True.')
#         if extra_fields.get('is_superuser') is not True:
#             raise ValueError('Superuser must have is_superuser=True.')

#         return self.create_user(email, **extra_fields)


# class User(models.Model):
#     username = None
#     email = models.EmailField(unique=True)
#     is_verified = models.BooleanField(default=False)
#     otp = models.CharField(max_length=6, null=True, blank=True)

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = []

#     objects = UserManager()

#     def __str__(self):
#         return f'{self.email}-{self.otp}'
#     pass

# from django.db import models
# from django.contrib.auth.models import AbstractUser, BaseUserManager, Group, Permission

# class UserManager(BaseUserManager):
#     def create_user(self, email, password=None):
#         if not email:
#             raise ValueError('Users must have an email address')
#         email = self.normalize_email(email)
#         user = self.model(email=email)
#         user.set_password(password)  # Hash the password
#         user.save(using=self._db)
#         return user

#     def create_superuser(self, email, password=None):
#         user = self.create_user(email, password)
#         user.is_admin = True
#         user.is_staff = True  # Set staff status for superuser
#         user.is_superuser = True  # Ensure superuser status
#         user.save(using=self._db)
#         return user

# class User(AbstractUser):  # Inherit from AbstractUser
#     email = models.EmailField(unique=True)
#     otp = models.CharField(max_length=6, blank=True, null=True)  # Keep OTP
#     is_verified = models.BooleanField(default=False)  # Verification status

#     # The groups and user_permissions fields come from AbstractUser
    
#     objects = UserManager()

#     # Specify the field to use for login
#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = []  # Email is the only required field for user creation

#     def __str__(self):
#         return self.email

# from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
# from django.db import models

# class UserManager(BaseUserManager):
#     def create_user(self, email, password=None, **extra_fields):
#         """
#         Creates and saves a User with the given email and password.
#         """
#         if not email:
#             raise ValueError('The Email field must be set')
#         email = self.normalize_email(email)
#         user = self.model(email=email, **extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_superuser(self, email, password=None, **extra_fields):
#         """
#         Creates and saves a superuser with the given email and password.
#         """
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_superuser', True)

#         return self.create_user(email, password, **extra_fields)


# class User(AbstractBaseUser, PermissionsMixin):
#     email = models.EmailField(unique=True)
#     is_active = models.BooleanField(default=True)
#     is_staff = models.BooleanField(default=False)
    
#     # This is where you set the field Django will use to log the user in
#     USERNAME_FIELD = 'email'
    
#     # Fields that are required when creating a superuser via createsuperuser command
#     REQUIRED_FIELDS = []

#     objects = UserManager()

#     def __str__(self):
#         return self.email
    
# from django.db import models
# from django.utils import timezone

# class UserOTP(models.Model):
#     email = models.EmailField()
#     otp = models.CharField(max_length=6)  # Assuming OTP is 6 digits
#     timestamp = models.DateTimeField(default=timezone.now)

#     def __str__(self):
#         return f'{self.email} - {self.otp}'


from django.db import models

# class User(models.Model):
#     username = models.CharField(max_length=150, unique=True)
#     email = models.EmailField(unique=True)
#     first_name = models.CharField(max_length=30)
#     last_name = models.CharField(max_length=30)
#     date_joined = models.DateTimeField(auto_now_add=True)
#     is_active = models.BooleanField(default=True)

#     def __str__(self):
#         return self.username

# from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
# from django.db import models

# class UserManager(BaseUserManager):
#     def create_user(self, email, username, password=None):
#         if not email:
#             raise ValueError('Users must have an email address')
#         if not username:
#             raise ValueError('Users must have a username')

#         user = self.model(
#             email=self.normalize_email(email),
#             username=username,
#         )
#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_superuser(self, email, username, password=None):
#         user = self.create_user(
#             email=email,
#             username=username,
#             password=password,
#         )
#         user.is_admin = True
#         user.save(using=self._db)
#         return user


# class User(models.Model):
#     email = models.EmailField(unique=True)
#     username = models.CharField(max_length=150, unique=True)
#     date_joined = models.DateTimeField(auto_now_add=True)
#     is_active = models.BooleanField(default=True)
#     is_admin = models.BooleanField(default=False)
#     is_verified = models.BooleanField(default=False)

#     objects = UserManager()

#     USERNAME_FIELD = 'email'  # Use 'email' for authentication
#     REQUIRED_FIELDS = ['username']  # This is what was missing

#     def __str__(self):
#         return self.email

#     def has_perm(self, perm, obj=None):
#         return True

#     def has_module_perms(self, app_label):
#         return True

#     @property
#     def is_staff(self):
#         return self.is_admin

# from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
# from django.db import models

# class UserManager(BaseUserManager):
#     def create_user(self, email, username, password=None):
#         if not email:
#             raise ValueError('Users must have an email address')
#         if not username:
#             raise ValueError('Users must have a username')

#         user = self.model(
#             email=self.normalize_email(email),
#             username=username,
#         )
#         user.set_password(password)  # This hashes the password
#         user.save(using=self._db)
#         return user

#     def create_superuser(self, email, username, password=None):
#         user = self.create_user(
#             email=email,
#             username=username,
#             password=password,
#         )
#         user.is_admin = True
#         user.save(using=self._db)
#         return user

# class User(AbstractBaseUser):
#     email = models.EmailField(unique=True)
#     username = models.CharField(max_length=150, unique=True)
#     password = models.CharField(max_length=128, default=True)
#     date_joined = models.DateTimeField(auto_now_add=True)
#     is_active = models.BooleanField(default=True)
#     is_admin = models.BooleanField(default=False)
#     is_verified = models.BooleanField(default=False)

#     objects = UserManager()

#     USERNAME_FIELD = 'email'  # Use 'email' for authentication
#     REQUIRED_FIELDS = ['username']  # This is what was missing

#     def __str__(self):
#         return self.email

#     def has_perm(self, perm, obj=None):
#         return True

#     def has_module_perms(self, app_label):
#         return True

#     @property
#     def is_staff(self):
#         return self.is_admin

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models

class UserManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        if not username:
            raise ValueError('Users must have a username')

        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )
        user.set_password(password)  # This hashes the password
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password=None):
        user = self.create_user(
            email=email,
            username=username,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=150, unique=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'  # Use 'email' for authentication
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin



