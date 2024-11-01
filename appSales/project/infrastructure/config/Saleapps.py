from django.apps import AppConfig
from entities import sales

class DjangoappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'sales'
