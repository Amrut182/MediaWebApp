from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import UserLoginForm
from django.contrib.auth import authenticate, login, logout

# creating a signup view
def signup(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f'Account created for {username}!')
            return redirect('login')
    else:
        form  = UserLoginForm()
    return render(request,'users/signup.html',{'form':form})



# def login(request):
#     if request.method == "POST":
#         form = UserLoginForm(request.POST)
#         if not form.is_valid():
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password1')
#             user = authenticate(username=username, password=password)
#             if user is not None:
#                 if user.is_active:
#                     login(request, user)
#                     return redirect('home')
#             else :
#                 messages.success(request,f'ERROR {username} {pass}')
#         else:
#             messages.success(request,f'ERROR2')
#     return render(request,'users/login.html',{'form':form})
