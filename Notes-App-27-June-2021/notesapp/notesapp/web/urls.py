from django.contrib import admin
from django.urls import path

from notesapp.web import views

# 3.	Routes
# •	http://localhost:8000/ - home page
# •	http://localhost:8000/add - add note page
# •	http://localhost:8000/edit/:id - edit note page
# •	http://localhost:8000/delete/:id - delete note page
# •	http://localhost:8000/details/:id - note details page
# •	http://localhost:8000/profile - profile page


urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('add/', views.add_note, name='add_note'),
    path('edit/<int:pk>', views.edit_note, name='edit_note'),
    path('delete/<int:pk>', views.delete_note, name='delete_note'),
    path('details/<int:pk>', views.details_note, name='details_note'),
    path('profile/', views.profile_view, name='profile_view'),
    path('profile/delete/', views.profile_delete, name='profile_delete'),
]
