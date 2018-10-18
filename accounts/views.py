from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

def signup(request):
    if request.method== 'POST':
        #使用者想要申請帳號
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.get(username=request.POST['username'])
                return render(request, 'accounts/signup.html', {'error':'Username has already been taken!'})
            except User.DoesNotExist:
                user = User.objects.create_user(request.POST['username'],password=request.POST['password1'])
                auth.login(request,user)
                return redirect('home')
            #這邊也可以用=password2，因為進到畫面後password1=2
        else:
            return render(request, 'accounts/signup.html', {'error':'The password must match!'})
    else:
        # 使用者想輸入資訊
        return render(request, 'accounts/signup.html')

    return render(request, 'accounts/signup.html')

def login(request):
    if request.method =='POST':
        user = auth.authenticate(username=request.POST['username'],password=request.POST['password'])
        if user is not None:
            auth.login(request,user)
            return redirect('home')
        else:
            return render(request, 'accounts/login.html', {'error':'Hey! The username or password is wrong!'})
    else:
        return render(request, 'accounts/login.html')

def logout(request):
    if request.method== 'POST':
        auth.logout(request)
        return redirect('home')
    return render(request, 'accounts/signup.html')
#注意signout要帶回原homepage
