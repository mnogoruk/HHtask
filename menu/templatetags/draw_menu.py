from django import template

register = template.Library()


@register.inclusion_tag('menu_list.html')
def draw_menu(menu_name):
    return {'menu_name': ''}

