from django.apps import AppConfig


class OpdaConfig(AppConfig):
    name = 'opda'

    def ready(self):
        import opda.signals