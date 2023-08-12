from django.contrib import admin
from django.urls import path

from online_library.web import views

# 3.	Routes
# •	http://localhost:8000/ - home page
# •	http://localhost:8000/add/ - add book page
# •	http://localhost:8000/edit/:id - edit book page
# •	http://localhost:8000/details/:id - book details page
# •	http://localhost:8000/profile/ - profile page
# •	http://localhost:8000/profile/edit/ - edit profile page
# •	http://localhost:8000/profile/delete/ - delete profile page

urlpatterns = [
    path('', views.home_page, name="home_page"),
    path('add/', views.add_book, name="add_book"),
    path('edit/<int:pk>/', views.edit_book, name="edit_book"),
    path('details/<int:pk>/', views.book_details, name="book_details"),
    path('delete/<int:pk>/', views.book_delete, name='book_delete'),
    path('profile/', views.profile_page, name="profile_page"),
    path('profile/edit/', views.edit_profile, name="edit_profile"),
    path('profile/delete/', views.delete_profile, name="delete_profile"),
]
