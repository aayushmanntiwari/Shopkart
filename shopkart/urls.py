"""shopkart URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from Login.views import password
from Products.views import color_options_based_on_size

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('Home.urls')),
    path('login/',include('Login.urls')),
    path('register/',include('Register.urls')),
    path('logout/',include('Logout.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('passwordvalidation/(?P<pk>[0-9]+)/<num>/$',password,name='passwordvalidation'),
    path('seller/',include('seller.urls')),
    path('',include('Products.urls')),
    path('',include('Orders.urls')),
    path('ajaxcolor/',color_options_based_on_size,name='ajaxcolor')
]


urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
