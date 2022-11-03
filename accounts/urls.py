
from django.urls import path

from accounts import views

urlpatterns = [
    path('signin/', views.signin, name='signin'),
    path('signout/', views.signout, name='signout'),
    path('main/', views.get_main_page, name='get_main_page'),
    path('upload/users/', views.create_new_users, name='create_new_users')
]
