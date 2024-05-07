from django.contrib import admin
from django.urls import path, include
from . import views

# Define URL patterns for the application
urlpatterns = [
    path('', views.home, name="home"),  # Home page
    path('signup', views.signup, name="signup"),  # User signup
    path('signin', views.signin, name="signin"),  # User signin
    path('signout', views.signout, name="signout"),  # User signout
    path('user/posts/', views.user_posts, name='user_posts'),  # User's posts
    path('user/create_post/', views.create_post, name='create_post'),  # Create a new post
    path('about/', views.about, name='about'),  # About page
    path('contact/', views.contact, name='contact'),  # Contact page
]
