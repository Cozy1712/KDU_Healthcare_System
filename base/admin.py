from django.contrib import admin

# Register your models here.
from .models import Room, Hospital, Specialisation, Message, RegisterUser, User, ChatTable, Appointment, Prescription
admin.site.register(User)
admin.site.register(Room)
admin.site.register(Hospital)
admin.site.register(Specialisation)
admin.site.register(Message)
admin.site.register(RegisterUser)
admin.site.register(ChatTable)
admin.site.register(Appointment)
admin.site.register(Prescription)