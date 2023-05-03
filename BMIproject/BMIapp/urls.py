from django.urls import path
from . import views

app_name='bmi'
urlpatterns = [
    path('', views.home,name='home'),
    path('cal/', views.cal,name='cal'),
    path('history/', views.history,name='history'),
    path('table/', views.table,name='table'),


]