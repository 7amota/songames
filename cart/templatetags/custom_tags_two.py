from django import template
import datetime
register = template.Library()
@register.simple_tag
def get_date():
    return datetime.datetime.now().strftime("%d/%m/%Y")