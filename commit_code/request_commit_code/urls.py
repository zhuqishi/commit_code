from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # ex: /request_commit_code/
    path('', views.user_login, name='user_login'),
    path('login/', views.user_login, name='user_login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='request_commit_code/logout.html'), name='user_logout'),
    path('<user_name>', views.show_user_request_list, name='show_user_request_list'),
]