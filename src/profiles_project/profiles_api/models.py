from django.db import models                                #default
from django.contrib.auth.models import AbstractBaseUser     #imported
from django.contrib.auth.models import PermissionsMixin     #imported

# Create your models here.

class UserProfile(AbstractBaseUser, PermissionsMixin):
    #Represents a user profile inside our system.

    email = models.EmailField(max_length=255, unique=True)     #unique-- only one email per profile in the project
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    #ObjectManager is a class used to help manage the profile giving 
    # additional functionality like creating a admin user or creting a regular user

    objects =  UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    #Helper Functions

    def get_full_name(self):
        #Used to get users full name.
        return self.name


    def get_short_name(self):
        #Used to get users short name.
        return self.name

    #In python if we need to print user Profile object in a nice way we need to tell it which field it has to look into.

    def __str__(self):
        #Django uses it when it needs to convert the object to string
        return self.email

    