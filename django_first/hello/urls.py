from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:name>",views.greet_render, name="greet_render"),
    path("dhana", views.dhana, name="dhana"),
    path("anna", views.anna, name="anna"),
    path("index",views.index, name="index"),
    path("index_render",views.index_render, name="index_render"),
    path("<str:name>", views.greet, name="greet")
]