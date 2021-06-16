from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),    
    path('logout/', views.logout, name='logout'),
    path('login/', views.login_page, name='login'),
    path('register/', views.register, name='register'),
    path('details_lines/', views.details_Lines, name='lines'),
    path('details_pylons/', views.details_Pylons, name='pylons'),
    path('details_cabinets/', views.details_Cabinets, name='cabinets'),
]