from django.urls import path
from pushpa.views import *
app_name='anything'
urlpatterns=[
    path('alluarjun/',alluarjun,name='alluarjun'),
]
