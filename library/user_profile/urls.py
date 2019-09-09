from django.urls import path, include
from . import views

urlpatterns = [
    path('<int:id>',views.user_profile,name = 'user_profile'),
    path('removeBook/<int:id>',views.removeBook,name = 'removeBook'),
    path('editBook/<int:id>',views.editBook,name = 'editBook'),
]