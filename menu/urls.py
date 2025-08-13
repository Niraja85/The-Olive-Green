from django.urls import path
from . import views

urlpatterns = [
    path('menu/', views.menu_view, name='menu'),
    path('create_menu/', views.CreateMenuView.as_view(), name='create_menu'),
    path('create_menu_items/', views.CreateMenuItemsView.as_view(),
         name='create_menu_items'),
    path('delete/<slug:pk>', views.DeleteMenuItemView.as_view(),
         name='delete_menu'),
    path('editmenu/<slug:pk>', views.EditMenuItemView.as_view(),
         name='edit_menu'),
    path('manage_menu/', views.ManageMenuView.as_view(), name='manage_menu'),
]
