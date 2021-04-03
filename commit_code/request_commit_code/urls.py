from django.urls import path

from . import views

urlpatterns = [
    # ex: /request_commit_code/
    path('', views.show_request, name='show_request'),
    # ex: /request_commit_code/login/
    #path(r'^$', views.show_request, name='show_request'),
]