from django.contrib import admin
from django.urls import path
from movieapp import views
app_name='movieapp'


urlpatterns = [
    path('',views.home,name='home'),
    path('movie/<int:movie_id>/',views.details,name='details'),
    path('add/',views.add_movie,name='add_movie'),
    path('update/<int:id>/',views.update,name='update'),
    path('delete/<int:id>/',views.delete,name='delete')
]
