from django.shortcuts import render
from django.views import View
from .models import MenuItem


class MenuView(View):
    def get(self, request, menu_name):
        menu_items = MenuItem.objects.filter(name=menu_name)
        context = {'menu_items': menu_items}
        return render(request, 'main/menu.html', context)


def index(request):
    return render(request, 'main/index.html')
