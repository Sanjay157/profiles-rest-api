from django.db import models                                #default
from django.contrib.auth.models import AbstractBaseUser     #imported
from django.contrib.auth.models import PermissionsMixin     #imported #Allows to give permission as to what and what not to do for user model
from django.contrib.auth.models import BaseUserManager      #imported to work with Object Manager/UserProfileManager
# Create your models here.

class UserProfileManager(BaseUserManager):
    #Helps Django to work with our custom user model.

    def create_user(self, email, name, password=None):              #STANDARD USER
        #Create a new user profile object.

        if not email:                                               #if the email field is blank then an error will be raised
            raise ValueError("User must have a vaild email ID")

        email = self.normalize_email(email)                         #normalize will convert all the characters to lowercase letters
        user = self.model(email=email, name=name)

        user.set_password(password)
         

        return user 

    def create_superuser(self, email, name, password):              #SUPERUSER
        #Creates and saves a new superuser with the given details.

        user = self.create_user(email, name, password)  

        user.is_superuser = True
        user.is_staff = True

        user.save(using = self._db)
        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    #Represents a user profile inside our system.

    email = models.EmailField(max_length=255, unique=True)     #unique-- only one email per profile in the project
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    #ObjectManager is a class used to help manage the profile giving 
    # additional functionality like creating a admin user or creating a regular user

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

