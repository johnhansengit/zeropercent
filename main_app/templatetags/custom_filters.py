from django import template

register = template.Library()

# Returns the value turned into a list.
@register.filter(name='split')
def split(value, key):
    return value.split(key)
