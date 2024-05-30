# tasks/urls.py
from django.urls import path
from .import views
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    
    path('home', views.home, name='home'),
    path('add/', views.add_task, name='add_task'),
    path('edit/<int:task_id>/', views.edit_task, name='edit_task'),
    path('delete/<int:task_id>/', views.delete_task, name='delete_task'),
    path('view/', views.view_tasks, name='view_tasks'),
    path('login/', views.handlelogin, name='login'),
    path('', views.signup, name='signup'),
    path('logout/', views.logout_view, name='logout'),


]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)



