from math import floor

from django import template

register = template.Library()

@register.filter
def seconds_to_mm_ss(seconds):
    minutes = floor(seconds / 60)
    seconds = floor(seconds - (minutes * 60))
    return '%d:%02d' % (minutes, seconds)
