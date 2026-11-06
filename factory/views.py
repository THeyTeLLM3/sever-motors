
from django.shortcuts import render


def home(request):
    return render(request, "factory/home.html")


def about(request):
    return render(request, "factory/about.html")


def contacts(request):
    return render(request, "factory/contacts.html")


def directions(request):
    return render(request, "factory/directions.html")


def vehicles(request):
    return render(request, "factory/vehicles.html")


def production(request):
    return render(request, "factory/production.html")
