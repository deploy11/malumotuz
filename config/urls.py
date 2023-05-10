"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from main.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home,name='home'),
    path('malumot/<int:pk>/',detail.as_view(),name="details"),
    path('nomi-bo`yicha/',nomi,name='nomi'),
    path('matni-bo`yicha/',matn,name='matn'),
    path('audio-file-bo`yicha',audio,name='audio'),
    path('category/',categores,name='categ'),
    path('nur-dashboard/',dashboard,name='dash'),
    path('nur-dashboard/new/',MalumotCreate.as_view(),name='new'),
    path('nur-dashboard/<int:pk>/update/',MalumotUpdate.as_view(),name='update'),
    path('nur-dashboard/<int:pk>/delete/',MalumotDelete.as_view(),name='delete'),
    path('malumot-admin/<int:pk>/',detailAdmin.as_view(),name="detaila"),
]
