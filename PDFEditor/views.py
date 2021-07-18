from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView
from PDFEditor.models import *
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from .forms import UserLoginForm, AddECP, SuperimposeFrom
from django.contrib.auth import login, logout

@login_required(redirect_field_name='login')
def index(request):
    bbs = Wotermark.objects.filter(user_main=request.user)
    #bbs = Wotermark.objects.get(user_main=request.user)
    bbs.order_by('-dataAdd')
    #bbs.filter(user_main="")
    context = {'bbs': bbs}
    return render(request, "PDFEditor/index.html", context)

def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = UserLoginForm()
    return render(request, 'PDFEditor/login.html', {"form": form})

@login_required(redirect_field_name='login')
def logout_view(request):
    logout(request)
    return redirect('login')

@login_required(redirect_field_name='login')
def addECP(request):
    if request.method == 'POST':
        form = AddECP(request.POST, request.FILES)
        if form.is_valid():
            incident = form.save(False)
            incident.user_main = request.user
            incident.save()
            return redirect('home') 
    else:
        form = AddECP()
    return render(request, 'PDFEditor/addECP.html', {"form": form})

@login_required(redirect_field_name='login')
def superimpose(request):
    if request.method == 'POST':
        form = SuperimposeFrom(request.POST, request.FILES, user=request.user)

        if form.is_valid():
            # Меленькая тонкость, это сохранит объект модели в переменную, но не в базу данных
            incident = form.save(False)
            incident.user_main = request.user
            incident.save()
            return redirect('home') 
    else:
        form = SuperimposeFrom(user=request.user)
    return render(request, 'PDFEditor/superimpose.html', {"form": form})
