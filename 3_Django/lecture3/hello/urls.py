from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("ira", views.ira, name="ira"),
    path("<str:name>", views.greet, name="greet")
]
