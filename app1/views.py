from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='login')
def HomePage(request):
    return render(request, 'home.html')

def SignupPage(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')
        
        if pass1 != pass2:
            context = {'error_message': 'Your password and confirm password are not the same!'}
            return render(request, 'signup.html', context)
        else:
            try:
                if not username  or not email:
                    context = {'error_message': 'Username cannot be empty!'}
                    return render(request, 'signup.html', context)
                elif not pass1  or not pass2:
                    context = {'error_message': 'Password  cannot be empty!'}
                    return render(request, 'signup.html', context) 
                my_user = User.objects.create_user(uname, email, pass1)
                my_user.save()
                return redirect('login')
            except Exception as e:
                context = {'error_message': f'An error occurred: {e}'}
                return render(request, 'signup.html', context)

    return render(request, 'signup.html')

def LoginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('pass')
           
        try:
            if not username :
                context = {'error_message': 'Username  cannot be empty!'}
                return render(request, 'login.html', context)
            elif not pass1 :
                context = {'error_message': 'Password  cannot be empty!'}
                return render(request, 'login.html', context) 
            user = authenticate(request, username=username, password=pass1)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                context = {'error_message': 'Username or Password is incorrect!!!'}
                return render(request, 'login.html', context)
        except Exception as e:
            context = {'error_message': f'An error occurred: {e}'}
            return render(request, 'login.html', context)

    return render(request, 'login.html')

def LogoutPage(request):
    try:
        logout(request)
    except Exception as e:
        context = {'error_message': f'An error occurred: {e}'}
        return render(request, 'home.html', context)
    return redirect('login')
