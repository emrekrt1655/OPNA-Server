from django.apps import AppConfig


class OptaConfig(AppConfig):
    name = 'opta'

    def ready(self):
        import opta.signals
