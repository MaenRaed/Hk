from django.shortcuts import render,HttpResponse,redirect
from .models import *
from django.contrib.auth import logout
from django.contrib import messages


def Home(request):
    return render(request,'index.html')

def Services(request):
    return render(request,'Services.html')

def Login(request):
    return render(request,'Login.html')

def Register(request):
    return render(request,'Register.html')

def Logout(request):
    return render(request,'index.html')


def Reg(request):
    request.session['username']=request.POST['user']
    User.objects.create(username=request.POST['user'],email=request.POST['email'],password=request.POST['pass'])
    messages.success(request, 'Registration successful!')  # Add this line after successful registration
    return redirect('/Home')

def Log(request):
    
    log_user=User.objects.filter(username=request.POST['user']) 

    if not log_user:
        request.session['error']="Invalid credentials!"
        return redirect("/Login")
    else:
        user=log_user[0]
        if user.password!=request.POST['pass']:
            request.session['error']="Invalid credentials!"
            return redirect("/Login")
        else:
            request.session['error']=""
            request.session['user']=user.username
            request.session['username']=request.POST['user']
            return redirect("/Home")

def Logout(request):
    request.session.clear()
    logout(request)
    return redirect('/Home')

def cBook(request):
    return render(request,'Book.html')

def Appointment(request):
    if 'username' in request.session and request.session['username']:
        Book.objects.create(Number=request.POST['phone'], Date=request.POST['date'], Time=request.POST['time'])
    else:
        Book.objects.create(Name=request.POST['name'], Email=request.POST['email'],
                            Number=request.POST['phone'], Date=request.POST['date'], Time=request.POST['time'])
    return redirect("/Home")

def History(request):
    all_appointments = Book.objects.all()
    context = {'appointments': all_appointments}
    return render(request, 'History.html', context)

def Contact(request):
    return render(request,'Contact.html')
