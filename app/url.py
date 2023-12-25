from django.urls import path
from . import views
urlpatterns = [
    path('',views.Home),
    path('Home',views.Home),
    path('Services',views.Services),
    path('Login',views.Login),
    path('Register',views.Register),
    path('Reg',views.Reg),
    path('Log',views.Log),
    path('Logout',views.Logout, name='logout'),
    path('Book',views.cBook),
    path('History',views.History),
    path('Appointment',views.Appointment),
    path('Contact',views.Contact),

    




]
