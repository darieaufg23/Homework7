from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('admin/add-product/', views.admin_add_product, name='admin_add_product'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
]