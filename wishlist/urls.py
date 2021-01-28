from . import views
from django.urls import path 


urlpatterns = [
    path('wishlist/',views.showwishlist,name="wishlist"),
    path('addtowishlist/',views.addtowishlist,name="addtowishlist"),
    path('deletewishlistitem/',views.deletewishitem,name="deletewishlistitem"),
]