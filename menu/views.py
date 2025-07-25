from django.views.generic import CreateView
from .models import Menu, MenuItem, MENU_CATEGORIES
from django.urls import reverse_lazy
from django.contrib import messages
from .forms import MenuForm


def menu_view(request):
    """ Create menu view to create a menu if user is staff """
    items = MenuItem.objects.prefetch_related()
    grouped_menu = {
        label: [item for item in items if item.category == key]
        for key, label in MENU_CATEGORIES
    }
    return render(request, 'menu/menu.html', {'grouped_menu': grouped_menu})

class CreateMenuView(CreateView):
    """ Create Menu View to create a menu if user is staff """
    model = Menu
    template_name = 'menu/create_menu.html'
    success_url = reverse_lazy('menu')
    form_class = MenuForm

    def form_valid(self, form):
        messages.success(self.request, 'Menu created successfully')
        return super().form_valid(form)
