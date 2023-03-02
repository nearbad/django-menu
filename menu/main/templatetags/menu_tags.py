from django import template
from ..models import MenuItem

register = template.Library()


def draw_menu(menu_name):
    menu_items = MenuItem.objects.filter(parent=None, name=menu_name)
    return {'menu_items': menu_items, 'menu_name': menu_name}


def draw_children(menu_item):
    return {'menu_item': menu_item}


register.inclusion_tag('main/menu.html')(draw_menu)
register.inclusion_tag('main/menu_children.html')(draw_children)
