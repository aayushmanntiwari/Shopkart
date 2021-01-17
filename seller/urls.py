from . import views
from django.urls import path

urlpatterns = [
    path('register/',views.seller_register),
    path('home/',views.sellerhomepage),
]