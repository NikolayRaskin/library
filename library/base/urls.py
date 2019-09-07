from django.urls import path, include
from . import views
from . import models

urlpatterns = [
    path('',views.index,name = 'index'),
    path('removeUser/<int:id>',views.removeUser,name = 'removeUser'),
    path('registration/',views.registration, name = 'registration'),
]