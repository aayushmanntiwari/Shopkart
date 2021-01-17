from . import views
from django.urls import path 


urlpatterns = [
   path('<greatgrandparent_name>/<grandparent_name>/<parent_name>/<child_name>/',views.products,name="products"),
   path('<greatgrandparent_name>/<grandparent_name>/<parent_name>/<child_name>/<product_name>/',views.product,name="product")
]