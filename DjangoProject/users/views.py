from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

# creating a signup view
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f'Account createf for {username}!')
            return redirect('home')
    else:
        form = UserCreationForm
    form  = UserCreationForm()
    return render(request,'users/signup.html',{'form':form})