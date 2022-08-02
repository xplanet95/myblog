from django import template
from blog.models import Category

register = template.Library()


@register.inclusion_tag('blog/menu_tpl.html')
def show_menu(menu_class='menu'):
    categories = Category.objects.all()  # noqa
    return {
        'categories': categories,
        'menu_class': menu_class,
    }

# @register.filter
# def addclass(field, css):
#         return field.as_widget(attrs={"class": css})
