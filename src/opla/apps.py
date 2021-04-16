from django.apps import AppConfig


class OplaConfig(AppConfig):
    name = 'opla'
    
    def ready(self):
        import opla.signals
