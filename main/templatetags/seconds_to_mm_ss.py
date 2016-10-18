from math import floor

from django import template

register = template.Library()


@register.filter
def minutes_part(seconds):
    return floor(seconds / 60)


@register.filter
def seconds_part(seconds):
    minutes = minutes_part(seconds)
    seconds = floor(seconds - (minutes * 60))
    return '%02d' % seconds
