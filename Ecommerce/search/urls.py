from django.urls import path
from django.contrib import admin
from . import views
app_name='search'

urlpatterns=[
    path('',views.search,name='search')
]