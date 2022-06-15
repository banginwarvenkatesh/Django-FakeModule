from . import views
from django.urls import path

urlpatterns =[
    path('sf/', views.ShowSalesman, name='show_url'),
    path('cr/', views.FakeData, name='create_url')
    ]