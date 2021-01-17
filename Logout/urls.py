from . import views
from django.urls import path

urlpatterns = [
    path('',views.logout,name="logout"),
]