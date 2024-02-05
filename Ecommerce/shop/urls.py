from django.contrib import admin
from django.urls import path
from . import views
app_name='shop'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.allcategory,name='home'),
    path('product/<p>', views.products, name='product'),
    path('details/<int:p>', views.details, name='details'),
    path('register', views.register, name='register'),
    path('login', views.u_login, name='login'),
    path('logout', views.u_logout, name='logout'),

]



