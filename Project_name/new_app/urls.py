from django.urls import path
from . import views

urlpatterns = [
    path('',views.fun,name='homepage'),
    path('update',views.update,name='update'),
    path('naming',views.naming,name='named')
]