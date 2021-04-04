from django.urls import path

from . import views

urlpatterns = [
    # ex: /request_commit_code/
    path('', views.show_users_list, name='show_users_list'),
    path('<user_name>', views.show_user_request_list, name='show_user_request_list'),
]