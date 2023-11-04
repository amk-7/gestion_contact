from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.contact_create, name='contact_create'),
    path('<int:pk>/update/', views.contact_update, name='contact_update'),
    path('<int:pk>/delete/', views.contact_delete, name='contact_delete'),
]
