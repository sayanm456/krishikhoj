from django.urls import path
from . import views

urlpatterns = [
    path("", views.farmer_form, name="farmer_insert"),
    path("list/", views.tractor_list, name="tractor_list")

]