from django.urls import path

from . import views

urlpatterns = [
    # ex: /request_commit_code/
    path('', views.index, name='index'),
    # ex: /request_commit_code/login/
    path('login', views.login, name='login'),
]