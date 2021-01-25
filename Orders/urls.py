from . import views
from django.urls import path


urlpatterns = [
    path('showcart/',views.showcart,name="showcart"),
    path('updateItem/',views.updateItem,name="updateItem"),
    path('deleteitem/',views.deleteorderitem,name='deleteitem')
]