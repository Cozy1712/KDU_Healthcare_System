from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Hospital(models.Model):
    name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name

class Specialisation(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class User(AbstractUser):
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField(unique=True, null=True)
    bio = models.TextField(null=True)
    status = models.CharField(null=True,max_length = 20)
    hospital = models.ForeignKey(Hospital, on_delete=models.SET_NULL, null=True)
    specialisation = models.ForeignKey(Specialisation, on_delete=models.SET_NULL, null=True) 
    avatar = models.ImageField(null=True, default="avatar.svg")
    certificate = models.ImageField(null=True, default="avatar.svg")
    gender = models.CharField(null=True,max_length = 20)
    card_number = models.CharField(null=True,max_length = 30)
    active = models.CharField(null=True,max_length = 3)
    created = models.DateTimeField(auto_now_add = True, null=True)



    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

class Room(models.Model):
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    specialisation = models.ForeignKey(Specialisation, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length = 200)
    description = models.TextField(null = True, blank = True)
    participants = models.ManyToManyField(User, related_name='participants', blank=True)
    updated = models.DateTimeField(auto_now = True)
    created = models.DateTimeField(auto_now_add = True)
    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.name


class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    body = models.TextField(null=True)
    updated = models.DateTimeField(auto_now = True)
    created = models.DateTimeField(auto_now_add = True)

    class Meta:
        ordering = ['updated','-created']

    def __str__(self):
        return self.body[0:50]

class RegisterUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length = 200)
    gender = models.CharField(max_length = 20)
    address = models.CharField(max_length = 200, null = True)
    phone = models.CharField(max_length = 20)
    status = models.CharField(null=True,max_length = 20)
    updated = models.DateTimeField(auto_now = True)
    created = models.DateTimeField(auto_now_add = True)
    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.name

    
class ChatTable(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    user1 = models.CharField(max_length = 200, null = True)
    user2 = models.CharField(max_length = 200, null = True)
    chat = models.CharField(max_length = 200, null = True)
    updated = models.DateTimeField(auto_now = True)
    created = models.DateTimeField(auto_now_add = True)
    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.chat

class Appointment(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    user1 = models.CharField(max_length = 200, null = True)
    user2 = models.CharField(max_length = 200, null = True)
    title = models.CharField(max_length = 200, null = True)
    date = models.CharField(max_length = 200, null = True)
    time = models.CharField(max_length = 200, null = True)
    appt_status = models.CharField(max_length = 20, null = True)
    created = models.DateTimeField(auto_now_add = True)
    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.title


class Prescription(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    user1 = models.CharField(max_length = 200, null = True)
    user2 = models.CharField(max_length = 200, null = True)
    title = models.CharField(max_length = 200, null = True)
    prescribed = models.CharField(max_length = 200, null = True)
    created = models.DateTimeField(auto_now_add = True)
    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.prescribed