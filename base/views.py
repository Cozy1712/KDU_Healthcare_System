from django.shortcuts import render, redirect
# for dynamic search
from django.db.models import Q
# ensure the users are logged in before allowing some responsibilities
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .models import Room, Hospital, Message, RegisterUser, Specialisation, User, ChatTable, Appointment, Prescription
from .form import RoomForm, UserForm, UserUpdateForm, DoctorUpdateForm, UserForm3, DoctorForm, UpdateUserForm, MyUserCreationForm, MyDoctorCreationForm, AppointmentForm, MyAdminCreationForm
from django.template.loader import get_template
from xhtml2pdf import pisa


from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string
# Create your views here.

# rooms = [
#     {'id':1, 'name': 'Lets code withs php'},
#     {'id':2, 'name': 'Introductions to Jquery'},
#     {'id':3, 'name': 'Ill Winds'},
# ] 

def registerUser(request):

    form = MyUserCreationForm()
    if request.method == 'POST':
        form = MyUserCreationForm(request.POST)
        username = request.POST.get('username').lower()
        email = request.POST.get('email').lower()
        password1 = request.POST.get('password1').lower()
        password2 = request.POST.get('password2').lower()
        mycard = request.POST.get('card_number')
        new_user = User.objects.filter(username = username)
        new_email = User.objects.filter(email = email)  
        new_card = User.objects.filter(card_number = mycard)  
        if new_user.count(): 
            messages.error(request, 'Error: Username Already taken!')
            return redirect('register')
        elif new_email.count(): 
            messages.error(request, 'Error: Email Already taken!')
            return redirect('register')
        elif new_card.count(): 
            messages.error(request, 'Error: Card Number Already taken!')
            return redirect('register')
        elif len(password1) < 8:
            messages.error(request, 'Error: Password length is short! Minimum of 6 Characters is required')
            return redirect('register')
        elif password1 and password2 and password1 != password2:
            messages.error(request, 'Error: Both Passwords are not the same!')
            return redirect('register')
        
        elif form.is_valid():
            user = form.save(commit=False)
            # convert the content of the username to lower case
            user.username = user.username.lower()
            user.status = 'patient'
            user.active = '1'
            # if user.password1 != user.password2:
            #     messages.error(request, 'Error: Both Passwords are not the same!')
            # if len(user.password1) < 8:
            #     messages.error(request, 'Error: Password length is too short!')
            user.save()
            # Send email on successful registration
            template_body = "Hello  "+request.POST.get('name')
            email = EmailMessage(
                'Thanks for chosing our services',
                template_body,
                settings.EMAIL_HOST_USER,
                [email],
            )
            email.fail_silently = False
            email.send()
            # log the user in automatically after the signup completed
            login(request, user)
            messages.success(request, 'Your Account was successfully created')
            return redirect('home')
        else:
            messages.error(request, 'Error Occured during registration')
            return redirect('register')
    context = {'form':form}
    return render(request,'base/login_register.html', context)

@login_required(login_url='login')
def createUser(request):
    form = UserForm3()
    if request.method == 'POST':
        # print(request.POST)
        form = UserForm3(request.POST)
        if form.is_valid():
            # user_detail = form.save(commit=False)
            # making sure that only the login user is able to create a room
            # user_detail.email.lower()
            # user_detail.user = request.user
            # user_detail.status = 'patient'
            # user_detail.save()
            form.save()
            return redirect('home')
    context = {'form': form}
    return render(request,'base/user_register.html', context)


def registerUserDoctor(request):
    form  = MyDoctorCreationForm()

    if request.method == 'POST':
        form = MyDoctorCreationForm(request.POST)
        username = request.POST.get('username').lower()
        email = request.POST.get('email').lower()
        password1 = request.POST.get('password1').lower()
        password2 = request.POST.get('password2').lower()
        new_user = User.objects.filter(username = username)
        new_email = User.objects.filter(email = email)  
        if new_user.count(): 
            messages.error(request, 'Error: Username Already taken!')
            return redirect('register-doctor')
        elif new_email.count(): 
            messages.error(request, 'Error: Email Already taken!')
            return redirect('register-doctor')
        elif len(password1) < 8:
            messages.error(request, 'Error: Password length is short! Minimum of 8 Characters is required')
            return redirect('register-doctor')
        elif password1 and password2 and password1 != password2:
            messages.error(request, 'Error: Both Passwords are not the same!')
            return redirect('register-doctor')
        elif form.is_valid():
            user = form.save(commit=False)
            # convert the content of the username to lower case
            user.username.lower()
            user.status = 'doctor'
            user.active = '1'
            user.save()
            # log the user in automatically after the signup completed
            login(request, user)
            messages.success(request, 'Your Account was successfully created')
            return redirect('home')
        else:
            messages.error(request, 'Error Occured during registration')
            return redirect('register-doctor')
    context = {'form':form}
    return render(request,'base/userDoc_register.html', context)


def registerUserAdmin(request):
    form  = MyAdminCreationForm()
    if request.method == 'POST':
        form = MyAdminCreationForm(request.POST)
        username = request.POST.get('username').lower()
        email = request.POST.get('email').lower()
        password1 = request.POST.get('password1').lower()
        password2 = request.POST.get('password2').lower()
        new_user = User.objects.filter(username = username)
        new_email = User.objects.filter(email = email)  
        if new_user.count(): 
            messages.error(request, 'Error: Username Already taken!')
            return redirect('register-admin')
        elif new_email.count(): 
            messages.error(request, 'Error: Email Already taken!')
            return redirect('register-admin')
        elif len(password1) < 8:
            messages.error(request, 'Error: Password length is short! Minimum of 8 Characters is required')
            return redirect('register-admin')
        elif password1 and password2 and password1 != password2:
            messages.error(request, 'Error: Both Passwords are not the same!')
            return redirect('register-admin')
        elif form.is_valid():
            user = form.save(commit=False)
            # convert the content of the username to lower case
            user.username.lower()
            user.status = 'admin'
            user.active = '1'
            user.save()
            # log the user in automatically after the signup completed
            login(request, user)
            messages.success(request, 'Your Account was successfully created')
            return redirect('view-records')
        else:
            messages.error(request, 'Error Occured during registration')
            return redirect('register-admin')
    context = {'form':form}
    return render(request,'base/userAdmin_register.html', context)

@login_required(login_url='login')
def createUserDoctor(request):
    form = DoctorForm()
    if request.method == 'POST':
        # print(request.POST)
        form = DoctorForm(request.POST)
        if form.is_valid():
            user_detail = form.save(commit=False)
            # making sure that only the login user is able to create a room
            user_detail.user = request.user
            user_detail.status = 'doctor'
            user_detail.save()
            return redirect('home')
    context = {'form': form}
    return render(request,'base/userDoc_create.html', context)


def loginPage(request):
    page = 'login'
    # redirect the logged in user to the home page while trying to access other url
    if request.user.is_authenticated:
        return redirect('home')
   
    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')
        
        try:

            user = User.objects.get(email=username)
        except:
            messages.error(request,'User does not exist')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            
            login(request, user)
            messages.success(request, 'Login Successfully')
            return redirect('home')
        else:
            messages.error(request, 'Username or Password does not exist')
            return redirect('login')
    context = {'page':page}
    return render(request, 'base/login_register.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')


def userProfile(request, key):
    user = User.objects.get(id=key)
    # _set.all() method is used to get all the children of that object
    rooms = user.room_set.all()
    room_messages = user.message_set.all()
    topics = Specialisation.objects.all()[:5]
    appointment = Appointment.objects.all().select_related('user')
    # check for a new appointment messages, and insert them into Appointment table
    if request.method == 'POST':
        appointment_create = Appointment.objects.create(
            user = request.user,
            user1 = request.user,
            user2 = user,
            fname = request.user.name,
            title = request.POST.get('title'),
            date = request.POST.get('date'),
            time = request.POST.get('time')
        )

    context = {'user':user, 'room':rooms, 'topics':topics, 'room_messages':room_messages,'appointment':appointment }
    return render(request, 'base/profile.html', context)


@login_required(login_url='login')
def updateUser(request):
    user = request.user
    form = UserUpdateForm(instance=user)

    if request.method == 'POST':
        form = UserUpdateForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('user-profile', key=user.id)

    return render(request, 'base/update-user.html', {'form': form})


@login_required(login_url='login')
def updateDoctor(request):
    user = request.user
    form1 = DoctorUpdateForm(instance=user)

    if request.method == 'POST':
        form1 = DoctorUpdateForm(request.POST, request.FILES, instance=user)
        if form1.is_valid():
            form1.save()
            return redirect('user-profile', key=user.id)

    return render(request, 'base/update-doctor.html', {'form1': form1})

@login_required(login_url='login')
def home(request):
    if request.user.status == 'admin':
        messages.success(request, 'Login Successfully')
        return redirect('view-records')
    # q = request.GET.get('q')
    # rooms = Room.objects.filter(topic__name=q)

    # searching/filtering the room by either topic name or the name of the user or the description of the room
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    rooms = Room.objects.filter(
        Q(specialisation__name__icontains=q) |
        Q(name__icontains=q) |
        Q(description__icontains=q)
        )

    topics = Specialisation.objects.all()[0:5]
    # count the number of rooms found from the searcch result
    room_count = rooms.count()
    # filter down the room messages based on the q operator
    room_messages = Message.objects.filter(Q(room__specialisation__name__icontains=q))
    # return HttpResponse('HomePage')
    context = {'room':rooms, 'topics':topics, 'room_count':room_count, 'room_messages':room_messages}
    return render(request,'base/home.html', context)

def room(request, key):
    # rom = None
    # for i in rooms:
    #     if i['id'] == int(key):
    #         rom = i
    rom = Room.objects.get(id=key)
    # get all the messages that belongs to this room
    # .order_by('-created') is used to rearrange the posted messages in descending order
    get_message = rom.message_set.all().order_by('-created')
    participants = rom.participants.all()
    

    # check for a new post messages, and insert them into Message table
    if request.method == 'POST':
        message = Message.objects.create(
            user = request.user,
            room = rom,
            body = request.POST.get('body')
        )
        # add participants to room table//very optional
        rom.participants.add(request.user)
        return redirect('room', key=rom.id)
    context = {'rom':rom, 'get_message':get_message, 'participants':participants}
    return render(request, 'base/room.html', context)


@login_required(login_url='login')
def createRoom(request):
    form = RoomForm()
    specialty = Specialisation.objects.all()
    if request.method == 'POST':
        # spec_name = request.POST.get('room_spec')
        # name, created = Specialisation.objects.get_or_create(name = spec_name)
        specialty_n = request.POST.get('specialty_name')
        specialisation, created = Specialisation.objects.get_or_create(name = specialty_n)
        inserRoom = Room.objects.create(
            host = request.user,
            specialisation = specialisation,
            name = request.POST.get('name').capitalize(),
            description = request.POST.get('description'),
        )
        if inserRoom:
            messages.success(request, 'Consultation Room Successfully Created')
            return redirect('home')
        # form = RoomForm(request.POST)
        # if form.is_valid():
        #     room = form.save(commit=False)
            # making sure that only the login user is able to create a room
            # room.host = request.user
            # room.name = reg.specialisation
            # room.save()
        return redirect('home')
    context = {'form': form,'specialty':specialty}
    return render(request, 'base/room_form.html', context)


@login_required(login_url='login')
def updateRoom(request, key):
    room = Room.objects.get(id=key)
    form = RoomForm(instance=room)
    specialty = Specialisation.objects.all()
    if request.user != room.host:
        return HttpResponse('Your are not allowed here!!')

    if request.method == 'POST':
        specialty_n = request.POST.get('specialty_name')
        specialisation, created = Specialisation.objects.get_or_create(name = specialty_n)
        room.name = request.POST.get('name')
        room.specialisation = specialisation
        room.description = request.POST.get('description')
        room.save()
        messages.success(request, 'Consultation Room Successfully Created')
        return redirect('home')

    context = {'form': form, 'specialty':specialty, 'room': room}
    return render(request, 'base/room_form.html', context)


# ensure the user login before they can perfom the operations below, if not redirect them to login page
@login_required(login_url='login')

def deleteRoom(request, key):
    room = Room.objects.get(id=key)
    # User should not be able to delete the message unless they belong to that room
    if request.user != room.host:
        return HttpResponse('You are not allowed to delete anything here')
    if request.method == 'POST':
        room.delete()
        messages.success(request, 'Consultation Room Successfully Deleted')
        return redirect('home')
    return render(request, 'base/delete.html', {'obj':room})


@login_required(login_url='login')

def deleteMessage(request, key):
    message = Message.objects.get(id=key)
    # User should not be able to delete the message unless they belong to that room
    if request.user != message.user:
        return HttpResponse('You are not allowed to delete anything here')
    if request.method == 'POST':
        message.delete()
        messages.success(request, 'Successfully Deleted')
        return redirect('home')
    return render(request, 'base/delete.html', {'obj':message})


def loginUser(request):
    page = 'login'
    # redirect the logged in user to the home page while trying to access other url
    if request.user.is_authenticated:
        return redirect('home')
   
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = RegisterUser.objects.get(email=email)
        except:
            messages.error(request,'User does not exist')
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Username or Password does note exist')

    context = {}
    return render(request, 'base/user_login.html', context)


def topicsPage(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    topics = Specialisation.objects.filter(name__icontains=q)
    return render(request, 'base/topics.html', {'topics': topics})

def activityPage(request):
    room_messages = Message.objects.all().order_by('-created')
    return render(request, 'base/activity.html', {'room_messages': room_messages})

# def prescribePage(request):
#     prescriptions = Prescription.objects.all().order_by('-created')
#     return render(request, 'base/prescriptions.html', {'prescriptions': prescriptions})

def privateChat(request, key):
    user3 = User.objects.get(id=key)
    if request.user.status == 'doctor':
        get_title = 'Dr.'
    if user3.status == 'doctor':
        get_title = 'Dr.'
    email = user3.email
    receiver = get_title+' '+user3.name
    sender = get_title+' '+request.user.name
    template_subject = 'Incoming message from '+sender
    get_message = ChatTable.objects.all()
    prescriptions = Prescription.objects.all()
    # _set.all() method is used to get all the children of that object
    # rooms = user.room_set.all()
    if request.method == 'POST':
        chat = ChatTable.objects.create(
            user = request.user,
            user1 = request.user,
            user2 = user3,
            chat = request.POST.get('body')
        )
        template_body = "Hello "+receiver+" below is the private chat sent to you by "+sender+" \nChat Details: "+request.POST.get('body')+'\n\nvisit www.kduhealthcare.com.ng to respond to this chat\n\nThanks!'
        email = EmailMessage(
            template_subject,
            template_body,
            settings.EMAIL_HOST_USER,
            [email],
            )
        email.fail_silently = False
        email.send()
    context = {'user3':user3,'get_message':get_message, 'prescriptions':prescriptions }
    return render(request, 'base/private_chat.html', context)

def prescribePage(request, key):
    user3 = User.objects.get(id=key)
    prescriptions = Prescription.objects.all()
    # prescriptions = Prescription.objects.all().order_by('-created')
    return render(request, 'base/prescriptions.html', {'user3':user3,'prescriptions': prescriptions})

@login_required(login_url='login')
def createAppointment(request, key):
    form = AppointmentForm()
    user = User.objects.get(id=key)
    if request.user.status == 'doctor':
        get_title = 'Dr.'
    if user.status == 'doctor':
        get_title = 'Dr.'
    email = user.email
    receiver = get_title+' '+user.name
    sender = get_title+' '+request.user.name
    template_subject = 'You have appointment with '+sender
    appointment = Appointment.objects.all()
    # check for a new appointment messages, and insert them into Appointment table
    if request.method == 'POST':
        appointment_create = Appointment.objects.create(
            user = request.user,
            user1 = request.user,
            user2 = user,
            title = request.POST.get('title'),
            date = request.POST.get('date'),
            time = request.POST.get('time')
        )
        if appointment_create:
            template_body = "Hello "+receiver+" below are the details of your appointment with "+sender+" \n\nAppointment Details: "+request.POST.get('title')+'\nDate and time: '+request.POST.get('date')+' '+(request.POST.get('time'))+'\n\nvisit www.kduhealthcare.com.ng to attend to this appointment\n\nThanks!'
            email = EmailMessage(
                template_subject,
                template_body,
                settings.EMAIL_HOST_USER,
                [email],
            )
            email.fail_silently = False
            email.send()
            messages.success(request, 'Appointment successfully created')
            return redirect('user-profile', key=user.id )
    context = {'user':user, 'appointment':appointment, 'form':form }
    # return redirect('user-profile', key=user.id )
    return render(request, 'base/appointment_form.html', context)



@login_required(login_url='login')
def updateAppointment(request, key):
    user = request.user
    appointment = Appointment.objects.get(id=key)
    form = AppointmentForm(instance=appointment)
    if request.method == 'POST':
        appointment.title = request.POST.get('title')
        appointment.date = request.POST.get('date'),
        appointment.time = request.POST.get('time')
        appointment.save()
        messages.success(request, 'Appointment successfully updated')
        return redirect('user-profile', key=user.id )

    context = {'form': form, 'appointment':appointment}
    return render(request, 'base/appointment_form.html', context)


@login_required(login_url='login')
def deleteAppointment(request, key):
    appoints = Appointment.objects.get(id=key)
    user = request.user
    # if request.user != appoints.user:
    #     return HttpResponse('You are not allowed to delete anything here')
    if request.method == 'POST':
        appoints.delete()
        messages.success(request, 'Appointment Deleted!')
        return redirect('user-profile', key=user.id )
    context = {'obj':appoints }
    return render(request, 'base/delete_appointment.html', context)


@login_required(login_url='login')
def createPrescription(request, key):
    user = User.objects.get(id=key)
    get_title = 'Dr.'
    email = user.email
    receiver = user.name
    sender = get_title+' '+request.user.name
    template_subject = 'Incoming message from '+sender
    if request.method == 'POST':
        prescription_create = Prescription.objects.create(
            user = request.user,
            user1 = request.user,
            user2 = user,
            title = request.POST.get('title'),
            prescribed = request.POST.get('prescribed')
        )
        if prescription_create:
            template_body = "Hello "+receiver+" below are the details of your prescriptions from "+sender+" \n\nTitle"+request.POST.get('title')+" \nDetails: "+request.POST.get('prescribed')+'\n\nvisit www.kduhealthcare.com.ng to download the PDF\n\nThanks!'
            email = EmailMessage(
                template_subject,
                template_body,
                settings.EMAIL_HOST_USER,
                [email],
            )
            email.fail_silently = False
            email.send()
            messages.success(request, 'Prescriptions successfully created')
            return redirect('user-chat-profile', key=user.id )
    context = {'user':user }
    return render(request, 'base/prescription_form.html',  context)

@login_required(login_url='login')
def deletePrescription(request, key):
    del_prescribe = Prescription.objects.get(id=key)
    user = request.user
    if request.method == 'POST':
        del_prescribe.delete()
        messages.success(request, 'Prescription Successfully Deleted')
        return redirect('user-chat-profile', key=user.id )
    context = {'obj':del_prescribe }
    return render(request, 'base/delete_prescription.html', context)

@login_required(login_url='login')
def showPrescription(request, key):
    prescribes = Prescription.objects.get(id=key)
    template_path = 'base/display_info.html'
    context = { 'prescribes':prescribes }
    response = HttpResponse(content_type = 'application/pdf')
    response['Content-Disposition'] = 'attachment; filename="prescriptions.pdf"'
    template = get_template(template_path)
    html = template.render(context)
    # Create pdf
    pisa_status = pisa.CreatePDF(
        html, dest=response
    )
    # message if there's error
    if pisa_status.err:
        return HttpResponse('Error Occurred <pre>' + html + '</pre>')
    
    return response


@login_required(login_url='login')
def usersComponent(request):
    get_all_users = User.objects.all()
    context = { 'get_all_users':get_all_users}
    return render(request, 'base/users_component.html', context)


@login_required(login_url='login')
def usersComponentAdmin(request):
    get_all_users = User.objects.all()
    specialty = Specialisation.objects.all()
    if request.method == 'POST':
        Specialisation.objects.create(
            name = request.POST.get('specialised')
        )
        messages.success(request, 'New Specialisation added!')
        return redirect('view-records')
    context = { 'get_all_users':get_all_users,'specialty':specialty}
    return render(request, 'base/admin.html', context)

@login_required(login_url='login')
def deleteSpecialisation(request, key):
    specialisation = Specialisation.objects.get(id=key)
    if request.method == 'POST':
        specialisation.delete()
        messages.success(request, 'Specialisation Deleted')
        return redirect('view-records')
    return render(request, 'base/delete.html', {'obj':specialisation})

@login_required(login_url='login')
def deleteUser(request, key):
    user1 = User.objects.get(id=key)
    if request.method == 'POST':
        user1.delete()
        messages.success(request, 'This User is Deleted')
        return redirect('view-records')
    return render(request, 'base/delete.html', {'obj':user1})    

@login_required(login_url='login')
def userProfileAdmin(request, key):
    cur_user = request.user
    user = User.objects.get(id=key)
    if request.method == 'POST':
        user.active = request.POST.get('valu')
        user.save()
        messages.success(request, 'User status successfully changed')
        return redirect('user-details', key=user.id )
    # if request.method == 'POST':
    #     if 'delete' in request.POST:
    #         user.delete()
    #         messages.success(request, 'User successfully deleted!')
    #         return redirect('user-details', key=user.id )
    context = {'user':user}
    return render(request, 'base/user_details.html', context)


@login_required(login_url='login')

def rejectAppointment(request, key):
    user = User.objects.get(id=key)
    if request.user.status == 'doctor':
        get_title = 'Dr.'
    if user.status == 'doctor':
        get_title = 'Dr.'
    email = user.email
    receiver = get_title+' '+user.name
    sender = get_title+' '+request.user.name
    template_subject = 'Your appointment with '+sender+ 'was declined'
    appointx = Appointment.objects.get(id=key)
    # for app in appointx:
    #     appoint_title = appointx.title
    if request.method == 'POST':
        appointx.appt_status = '0'
        appointx.save()
        template_body = "Hello "+receiver+" below are the details of your appointment that got declined by "+sender+" \n\nAppointment Details: "+get_title+'\n\nvisit www.kduhealthcare.com.ng to attend to this appointment\n\nThanks!'
        email = EmailMessage(
            template_subject,
            template_body,
            settings.EMAIL_HOST_USER,
            [email],
        )
        email.fail_silently = False
        email.send()
        messages.success(request, 'Appointment Rejected')
        return redirect('user-profile', key=request.user.id)
    return render(request, 'base/reject_appointment.html')

@login_required(login_url='login')
def acceptAppointment(request, key):
    appointx = Appointment.objects.get(id=key)
    if request.method == 'POST':
        appointx.appt_status = '1'
        appointx.save()
        messages.success(request, 'Appointment Accepted')
        return redirect('user-profile', key=request.user.id)
    return render(request, 'base/accept_appointment.html')

@login_required(login_url='login')
def googleSurvey(request):
    return render(request, 'base/my_survey.html')

@login_required(login_url='login')
def googleSurveyMobile(request):
    return render(request, 'base/my_survey_mobile.html')
