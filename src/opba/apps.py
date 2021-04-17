from django.apps import AppConfig


class OpbaConfig(AppConfig):
    name = 'opba'

    def ready(self):
        import opba.signals
