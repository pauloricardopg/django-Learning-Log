from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # Login page.
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    # Logout page.
    path('logout/', views.logout_view, name='logout'),
    # Pagina de cadastro.
    path('register/', views.register, name='register'),
]
