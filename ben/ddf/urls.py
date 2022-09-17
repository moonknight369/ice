from django.contrib import admin
from django.urls import path

from ddf import views

urlpatterns = [
    path ('',views.index,name="home"),
    path('artical/',views.artical,name="artical"),
    path('services/',views.service,name="service"),
    path('form/',views.fo,name="form")
]
