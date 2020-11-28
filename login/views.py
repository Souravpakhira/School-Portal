from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import CustomUser
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
# Create your views here.


def index(request):
    return render(request, "index.html")


def register(request):

    if request.method == 'POST':
        email = request.POST['email']
        phone = request.POST['phone']
        select = request.POST['user_type']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        # validating user
        if pass1 != pass2:
            messages.error(request, "Passwords do not match")
            print("pass not match")
            return redirect(register)

        myuser = CustomUser.objects.create_user(email, pass1)
        myuser.phonenumber = phone
        if select == 'Student':
            myuser.user_type = "S"
        else:
            myuser.user_type = "T"
        myuser.save()
        messages.success(
            request, "Your account has been successfully created!")
        return redirect(loginp)
    return render(request, 'register.html')


def loginp(request):
    if request.method == 'POST':
        email = request.POST['email']
        passwrd = request.POST['pass']
        user = authenticate(email=email, password=passwrd)
        if user is not None:
            print(user.user_type)
            if user.user_type == "T":
                login(request, user)
                return redirect(index)
            else:
                login(request, user)
                return redirect(index)
            # return render(request, 'studentd.html')
        else:
            messages.error(request, "Check credentail")
            # return render(request, 'teacherd.html')

    return render(request, 'login.html')


def handleLogout(request):
    logout(request)
    messages.success(request, "Logout successfully")
    return redirect(index)
