from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('destroy_session',views.clear_ses),
    path('double',views.double),
]
