from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import UserLoginForm

# creating a signup view
def signup(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f'Account createf for {username}!')
            return redirect('login')
    else:
        form  = UserLoginForm()
    return render(request,'users/signup.html',{'form':form})