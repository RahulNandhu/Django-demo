from django.contrib import admin
from django.urls import path
from app import views

app_name='app'


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('addmovies', views.addmovies, name='addmovies'),
    path('moreinfo/<int:p>', views.movie, name='moreinfo'),
    path('delete/<int:p>', views.delete, name='delete'),
    path('edit/<int:p>', views.edit, name='edit'),
]