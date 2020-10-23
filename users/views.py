from django.shortcuts import render,redirect,reverse
# from django.contrib.auth.forms import UserCreationForm
from django.contrib import  messages
from .forms import RegisterForm, UpdateForm
from django.contrib.auth.decorators import login_required
# Create your views here.
def index(request):
    return render(request, 'users/index.html',{})

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Account Created Successfully')
            return redirect(reverse('index'))
    else:
        form = RegisterForm()
    return render(request, 'users/register.html', {'form':form })


def update(request):
    form = UpdateForm()
    if request.method == 'GET':
        return render(request,'users/update.html',{'form':form })

@login_required
def profile(reqest):
    return render(reqest, 'users/profile.html',{})
