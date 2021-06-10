# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib.auth import logout as django_logout

# Create your views here.

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.views.generic import DetailView

from .models import Contacts


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def loginPage(request):
    form = UserCreationForm()
    context = {'form': form}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')

    return render(request, 'templates/login.html', context)


def register(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('loginPage')
            # return render(request, 'templates/loginPage.html')

    context = {'form': form}
    return render(request, 'templates/register.html', context)


def home(request):
    current_user = request.user
    contacts = Contacts.objects.filter(user=current_user)
    context = {'contacts': contacts}
    # for each in contacts:
    #     print(each.contact_name)
    #
    # if request.method == 'POST':
    #     return redirect("addContacts")

    return render(request, 'templates/home.html', context)


def landingPage(request):
    context = {}
    return render(request, 'templates/landingPage.html', context)


def addContacts(request):
    context = {}
    if request.method == 'POST':
        if request.POST.get('contactname'):
            newcontact = Contacts()
            newcontact.contact_name = request.POST.get('contactname')
            newcontact.user = request.user
            newcontact.save()
            contacts = Contacts.objects.filter(user=request.user)
            context = {'contacts': contacts}

            return render(request, 'templates/home.html', context)

    return render(request, 'templates/addContacts.html', context)

def deleteContact(request):
    current_user = request.user
    contacts = Contacts.objects.filter(user=current_user)
    context = {'contacts': contacts}
    # for each in contacts:
    #     print(each.contact_name)

    # if request.method == 'POST':
    #     return redirect("addContacts")

    if request.method == 'POST':
        if request.POST.get('delete_contact'):
            deleted_contact=Contacts.objects.filter(id=request.POST.get('delete_contact'))
            deleted_contact.delete()
            contacts = Contacts.objects.filter(user=request.user)
            context = {'contacts': contacts}

            return render(request, 'templates/home.html', context)

    return render(request, 'templates/deleteContact.html', context)

@login_required
def logout(request):
    if request.method=='POST':
        django_logout(request)
        return redirect('landingPage')
