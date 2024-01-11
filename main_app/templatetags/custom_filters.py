from django import template

register = template.Library()

# Returns the value turned into a list.
@register.filter(name='split')
def split(value, key):
    return value.split(key)

@register.filter(name='convert_to_hours_minutes')
def convert_to_hours_minutes(value):
    hours = value // 60
    minutes = value % 60
    if hours > 1:
        return f"{hours} hrs {minutes} mins"
    elif hours == 1:
        return f"{hours} hr {minutes} mins"
    else:
        return f"{minutes} mins"
