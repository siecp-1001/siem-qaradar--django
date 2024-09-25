from django.apps import AppConfig

class SecurityappConfig(AppConfig):
    name = 'securityapp'

    def ready(self):
        import securityapp.signals  # noqa
