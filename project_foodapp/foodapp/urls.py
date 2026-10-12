from django.urls import path
from . import views
urlpatterns = [
    path('', views.foodapp, name='foodapp')
]