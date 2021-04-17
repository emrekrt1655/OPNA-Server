from django.apps import AppConfig


class OpnaConfig(AppConfig):
    name = 'opna'

    def ready(self):
        import opna.signals
