from django.urls import path
from . import views

urlpatterns = [
    path('kazakhstan/', views.wrestling),
    path('kazakhstan1/',views.boxing),
    path('kazakhstan2/',views.footbal),
    path('',views.home),
    path('send/',views.send_message),
    path('kazakhstan3/', views.register, name = 'register'),
   ]