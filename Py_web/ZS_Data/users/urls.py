from . import views
from django.urls import path, re_path
from django.contrib.auth.views import LoginView

app_name = 'users'

urlpatterns = [
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', views.logout_view, name="logout")
]
