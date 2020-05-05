from django import template
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter
def danger_level(level):
    if level < 30:
        return mark_safe("<span style='color: green;'>Bajo</span>")
    elif level < 66:
        return mark_safe("<span style='color: orange;'>Medio</span>")
    else:
        return mark_safe("<span style='color: red;'>Alto</span>")