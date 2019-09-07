from django.urls import path, include
from . import views
from . import models

urlpatterns = [
    path('',views.index,name = 'index'),
    path('user_profile/<int:id>',views.user_profile,name = 'user_profile'),
    path('removeUser/<int:id>',views.removeUser,name = 'removeUser'),
    path('registration/',views.registration, name = 'registration'),
]