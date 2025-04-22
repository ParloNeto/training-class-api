from django.urls import path
from api.views.user_view import UserList

urlpatterns = [
    path('users/', UserList.as_view()),
]