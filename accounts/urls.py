"""cms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from . import views
from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [   
    path('',views.dashboard,name='dashboard'),
    path('customer/<int:pk_id>/',views.customer,name='customer'),
    path('products/',views.product,name='product'),
    path('order_form/<int:pk>/',views.orderform,name='orderform'),
    path('updates/<int:pk>/',views.updates,name='updates'),
    path('delete/<int:pk>/',views.deleteOrder,name='delete'),
    path('login/',views.account_login,name='login'),
    path('register/',views.register,name='register'),
    path('logout/',views.account_logout,name='logout'),
    path('user/',views.cms,name='cms'),
    path('accounts/',views.accountsettings,name='account'),
]
