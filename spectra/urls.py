"""spectra URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from spectra_core import views
urlpatterns = [
    path('delete_all_works', views.delete_all_works, name='delete_all_works'),
    path('create_work/', views.create_work, name='create_work'),
    path('create_work_success/', views.create_work_success, name='create_work_success'),
    path('work/<int:work_id>/', views.work, name='work'),
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('search/', views.search, name='search'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('create_account/', views.create_account, name='create_account'),
    path('accounts/login/', views.login, name='login'),
]
