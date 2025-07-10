"""
URL configuration for Mtodo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from todolist.views import index, add_page, add_note, note_details, update_page, update_note, delete_note, delete_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="index-page"),
    path('add/', add_page, name="add-page"),
    path('add_note/', add_note, name="add-note"),
    path('note_details/<str:slug>/', note_details, name="note_details"),
    path('update/<str:slug>/', update_page, name="update_page"),
    path('update_note/<str:slug>', update_note, name="update_note"),
    path('delete_note/<str:pk>', delete_note, name="delete_note"),
    path('delete_page/<str:pk>', delete_page, name="delete_page"),
]
