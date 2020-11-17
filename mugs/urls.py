from django.urls import path
from . import views

urlpatterns = [
    path('', views.mugs, name='mugs'),
    path('<mug_id>', views.mug_detail, name='mug_detail'),
]
