from django.apps import AppConfig


class SubscriberConfig(AppConfig):
    name = 'subscriber'

    def ready(self):
        import subscriber.signals
