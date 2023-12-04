from django.urls import path
from .views import add_user, get_users, hello, calc, login, get_notes

urlpatterns = [
    # For hello/?x=10
    # path('hello/', hello),
    # For hello/10
    path('hello/<int:number>', hello),
    path('calc', calc),
    path('users', get_users),
    path('add_user', add_user),
    path('login', login),
    path('notes', get_notes)
]