from django.views.generic import CreateView
from .models import Menu, MenuItem, MENU_CATEGORIES
from django.utils.decorators import method_decorator
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib import messages
from .forms import MenuForm, MenuItemForm
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin


def menu_view(request):
    """ Create menu view to create a menu if user is staff """
    items = MenuItem.objects.all()
    grouped_menu = {
        label: [item for item in items if item.category == key]
        for key, label in MENU_CATEGORIES
    }
    return render(request, 'menu/menu.html', {'grouped_menu': grouped_menu})

@method_decorator(staff_member_required, name='dispatch')
class CreateMenuView(LoginRequiredMixin, CreateView):
    """ Create Menu View to create a menu if user is staff """
    model = Menu
    template_name = 'menu/create_menu.html'
    success_url = '/menu/'
    form_class = MenuForm

    def form_valid(self, form):
        messages.success(self.request, 'Menu created successfully')
        return super().form_valid(form)


@method_decorator(staff_member_required, name='dispatch')
class CreateMenuItemsView(CreateView):
    """ Create Menu Items view to create menu items if user is staff"""
    model = MenuItem
    form_class = MenuItemForm
    template_name = 'menu/create_menu_items.html'
    success_url = '/menu/'

    def form_valid(self,form):
        messages.success(self.request, 'Item added to the menu successfully')
        return super().form_valid(form)
