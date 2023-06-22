from django import template 
import datetime
register = template.Library()
def get_first_name(name: str, arg) -> str:
    if arg == "first_name":
        return name.split(" ")[0]
register.filter('get_first_name', get_first_name)
