from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
# , PermissionsMixin
# from uuid import uuid4
from .manager import *

# class CustomeUserModelManager(BaseUserManager):
#     def create_user(self, username, email, password=None):
#         """
#         Creates a custom user with given fields
#         """

#         user = self.model(
#             username = username,
#             email = self.normalize_email(email),
#         )

#         user.set_password(password)
#         user.save(using = self._db)

#         return user
    

#     def create_superuser(self, username, email, password):
#         user = self.create_user(
#             username,
#             email,
#             password = password
#         )

#         user.is_staff = True
#         user.is_superuser = True
#         user.save(using = self._db)

#         return user
    
# class CustomUserModel(AbstractBaseUser, PermissionsMixin):
#     userId = models.CharField(max_length = 16, default = uuid4, primary_key = True, editable = False)
#     username = models.CharField(max_length = 16, unique = True, blank = False)
#     email = models.EmailField(max_length = 100, unique = True, null = False, blank = False)

#     USERNAME_FIELD = "username"
#     REQUIRED_FIELDS = ["email"]

#     active = models.BooleanField(default=True)
    
#     is_staff = models.BooleanField(default=False)
#     is_superuser = models.BooleanField(default=False)

#     created_on = models.DateTimeField(auto_now_add=True, blank = True, null = True)
#     updateds_at = models.DateTimeField(auto_now=True)

#     objects = CustomeUserModelManager()

#     class Meta:
#         verbose_name = "Custom User"

class CustomUser(AbstractBaseUser):
   
    
    email=models.EmailField(verbose_name='Email',max_length=30,unique=True)
    username=models.CharField(max_length=30,unique=True)     
    phone_number=models.CharField(max_length=50, unique=True)    
    date_joined=models.DateTimeField(verbose_name='Date Joined', auto_now_add=True)
    last_login=models.DateTimeField(verbose_name='Last Login', auto_now=True)
    is_admin=models.BooleanField(default=False)
    is_staff=models.BooleanField(default=False)
    is_active=models.BooleanField(default=True)
    is_superuser=models.BooleanField(default=False)
    # profile_image=models.ImageField(max_length=255,upload_to=,null=True,blank=True,default=)
    hide_email=models.BooleanField(default=True)

    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['username','phone_number']

    objects= UserManager()