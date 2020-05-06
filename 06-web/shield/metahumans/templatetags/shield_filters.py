from django import template
from django.utils.safestring import mark_safe

register = template.Library()

<<<<<<< HEAD
@register.filter
def danger_level(level):
    if level < 30:
        return mark_safe("<span style='color: green;'>Bajo</span>")
    elif level < 66:
        return mark_safe("<span style='color: orange;'>Medio</span>")
    else:
        return mark_safe("<span style='color: red;'>Alto</span>")
=======

@register.filter
def danger_level(level):
    if level < 30:
        color = 'green'
        label = 'Bajo'
    elif level < 66:
        color = 'orange'
        label = "Medio"
    else:
        color = 'red'
        label = "Alto"
    return mark_safe(f"<span style='color: {color};'>{label}</span>")

>>>>>>> e428c7a107ee62527848e4e4586cfbb34e7f6d16
