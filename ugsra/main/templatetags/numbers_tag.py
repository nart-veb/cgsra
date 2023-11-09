from django import template
from ..models import AbkhaziaNumber


register = template.Library()


@register.simple_tag()
def get_numbers():
    return AbkhaziaNumber.objects.order_by("title")
