from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()


@register.filter
@stringfilter
def remove_newlines(text):
    return text.replace('\n', ' ')
