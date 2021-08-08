from django import template

register = template.Library()

@register.filter(name='get_last')
def cut(value, arg):

    return value.split('/')[-1]
