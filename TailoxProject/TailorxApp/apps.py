from django.apps import AppConfig


class TailorxappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'TailorxApp'

    def ready(self):
        import TailorxApp.signals