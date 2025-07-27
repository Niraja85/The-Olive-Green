from django.urls import path
from . import views

urlpatterns = [
    path('menu/', views.menu_view, name='menu'),
    path('create_menu/', views.CreateMenuView.as_view(), name='create_menu'),
    path('create_menu_items/', views.CreateMenuItemsView.as_view(), name='create_menu_items'),
]