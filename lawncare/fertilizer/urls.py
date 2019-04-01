from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('fertilizers', views.fertilizers, name='fertilizers'),
    path('fertilizers/<int:fert_id>', views.detail, name='fertilizer'),
    path('fertilizers/<int:fert_id>/apply', views.apply, name='apply'),
]