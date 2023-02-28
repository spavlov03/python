from django.urls import path
from . import views

urlpatterns = [
    path('',views.root),
    path('shows/new',views.new),
    path('shows/add',views.add),
    path('shows',views.all),
    path('shows/<int:id>/destroy',views.delete),
    path('shows/<int:id>/edit',views.edit),
    path('shows/<int:id>/update',views.edit_show),
    path('shows/<int:id>',views.show)
]