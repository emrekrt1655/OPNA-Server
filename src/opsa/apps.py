from django.apps import AppConfig


class OpsaConfig(AppConfig):
    name = 'opsa'

    def ready(self):
        import opsa.signals