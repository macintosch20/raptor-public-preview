from django import template
from users.identity import display_name, greeting
register=template.Library()
register.filter('user_name',display_name)
register.filter('greeting',greeting)
