from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Gender(models.Model):
    gender_id = models.BigAutoField(primary_key=True, blank=False) #BIGINT NOT NULL AUTO_INCREMENT PRIMARY KEY
    gender = models.CharField(max_length=55, blank=False) #VARCHAR(55) NOT NULL
    date_created = models.DateTimeField(auto_now_add=True) #TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    date_updated = models.DateTimeField(auto_now=True) #TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMSTAMP

    class Meta:
        db_table = 'genders'



    def __str__(self):
        return self.gender

class User(models.Model):
    student_id = models.BigAutoField(primary_key=True, blank=False) #BIGINT NOT NULL AUTO_INCREMENT PRIMARY KEY
    first_name = models.CharField(max_length=55, blank=False) #VARCHAR(55) NOT NULL
    middle_name = models.CharField(max_length=55, blank=True) #VARCHR(55) DEFAULT NULL
    last_name = models.CharField(max_length=55, blank=False) #VARCHAR(55) NOT NULL
    age = models.IntegerField(blank=False) #INT NOT NULL
    birth_date = models.DateField(blank=False) #DATE NOT NULL
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE)
    math = models.IntegerField(blank=False)
    science = models.IntegerField(blank=False)
    english = models.IntegerField(blank=False)
    filipino = models.IntegerField(blank=False)
    history = models.IntegerField(blank=False)
    homeroom = models.IntegerField(blank=False)
    date_created = models.DateTimeField(auto_now_add=True) #TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'users'

class Teacher(AbstractUser):

    pass