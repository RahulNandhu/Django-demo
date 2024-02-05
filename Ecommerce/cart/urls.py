from django.contrib import admin
from django.urls import path
from . import views
app_name='cart'

urlpatterns = [
    path('addtocart/<p>',views.addtocart,name='addtocart'),
    path('cartview', views.cartview, name='cartview'),
    path('removecart/<p>', views.removecart, name='removecart'),
    path('cartdelete/<p>', views.cartdelete, name='cartdelete'),
    path('orderform', views.orderform, name='orderform'),
    path('yourorders', views.yourorders, name='yourorders'),

]