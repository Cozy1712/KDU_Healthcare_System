from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [

    path('', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('register/', views.registerUser, name="register"),
    path('update-user/', views.updateUser, name="update-user"),
    path('update-doctor/', views.updateDoctor, name="update-doctor"),
    path('register-doctor/', views.registerUserDoctor, name="register-doctor"),
    path('register-admin/', views.registerUserAdmin, name="register-admin"),
    path('create-doctor/', views.createUserDoctor, name="create-doctor"),
    path('home/', views.home, name="home"),
    path('room/<str:key>/', views.room, name="room"),
    path('specialisations/', views.topicsPage, name="specialisations"),
    path('delete-spec/<str:key>/', views.deleteSpecialisation, name="delete-spec"),
    path('delete-user/<str:key>/', views.deleteUser, name="delete-user"),
    path('activity/', views.activityPage, name="activity"),
    path('prescriptions/<str:key>/', views.prescribePage, name="prescriptions"),
    path('create-room/', views.createRoom, name="create-room"),
    path('create-user/', views.createUser, name="create-user"),
    path('login-user/', views.loginUser, name="login-user"),
    path('update-room/<str:key>/', views.updateRoom, name="update-room"),
    path('delete-room/<str:key>/', views.deleteRoom, name="delete-room"),
    path('create-appointment/<str:key>/', views.createAppointment, name="create-appointment"),
    path('update-appointment/<str:key>/', views.updateAppointment, name="update-appointment"),
    path('delete-appointment/<str:key>/', views.deleteAppointment, name="delete-appointment"),
    path('reject-appointment/<str:key>/', views.rejectAppointment, name="reject-appointment"),
    path('accept-appointment/<str:key>/', views.acceptAppointment, name="accept-appointment"),
    path('create-prescriptions/<str:key>/', views.createPrescription, name="create-prescriptions"),
    path('delete-prescriptions/<str:key>/', views.deletePrescription, name="delete-prescriptions"),
    path('user-prescribe-details/<str:key>/', views.showPrescription, name="user-prescribe-details"),
    path('delete-message/<str:key>/', views.deleteMessage, name="delete-message"),
    path('profile/<str:key>/', views.userProfile, name="user-profile"),
    path('chats-profile/<str:key>/', views.privateChat, name="user-chat-profile"),
    path('view-users/', views.usersComponent, name="view-users"),
    path('view-records/', views.usersComponentAdmin, name="view-records"),
    path('survey/', views.googleSurvey, name="survey"),
    path('survey-mobile/', views.googleSurveyMobile, name="survey-mobile"),
    path('user-details/<str:key>/', views.userProfileAdmin, name="user-details"),
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name="base/password_reset.html"), name = "reset_password"),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name="base/password_reset_sent.html"), name = "password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="base/password_reset_form.html"), name = "password_reset_confirm"),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="base/password_reset_done.html"), name = "password_reset_complete")
]