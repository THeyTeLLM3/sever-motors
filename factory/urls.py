from django.urls import path

from . import views

app_name = "factory"

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("about/contacts/", views.contacts, name="contacts"),
    path("about/directions/", views.directions, name="directions"),
    path("vehicles/", views.vehicles, name="vehicles"),
    path("production/", views.production, name="production"),
]
